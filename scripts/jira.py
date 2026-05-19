#!/usr/bin/env python3
"""Small Jira Cloud CLI for comments and worklogs.

Credentials are read from environment variables and, by default, from
scripts/jira/.env if that file exists.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_ENV_FILE = ROOT / ".env"
# DEFAULT_ENV_FILE = ROOT / "scripts" / "jira" / ".env"
APP_CONFIG: dict[str, str] = {}
HELP_EPILOG = """examples:
  python scripts/jira.py cloud-id
  python scripts/jira.py check-auth
  python scripts/jira.py scopes
  python scripts/jira.py list-issues P1732 --max 50
  python scripts/jira.py list-assignee --me --project P1732 --max 50
  python scripts/jira.py comment P1732-800 "Implemented validation changes."
  python scripts/jira.py worklog P1732-800 30m "Development work." --started "2026-05-19 11:00"
  python scripts/jira.py ai-contribution P1732-800 25
  python scripts/jira.py percent-done P1732-800 75
  echo "multi-line comment" | python scripts/jira.py comment P1732-800
"""
AI_CONTRIBUTION_FIELD_NAME = "AI contribution"
PERCENT_DONE_FIELD_NAME = "%Done"
REQUIRED_SCOPE_HELP = """Required Jira scopes for this script:
    SCOPES
    
    Read
    -------------------------------------
    read:audit-log:jira
    read:avatar:jira
    read:comment:jira
    read:comment.property:jira
    read:field:jira
    read:field-configuration:jira
    read:group:jira
    read:issue:jira
    read:issue.changelog:jira
    read:issue-security-level:jira
    read:issue-details:jira
    read:issue.vote:jira
    read:issue-worklog:jira
    read:issue-worklog.property:jira
    read:issue-meta:jira
    read:jira-user
    read:project-role:jira
    read:project:jira
    read:status:jira
    read:user:jira
    
    Write
    -------------------------------------
    write:comment:jira
    write:field:jira
    write:issue-worklog:jira
    write:issue-worklog.property:jira
    write:issue:jira

  """
ISSUE_SCOPE_HELP = f"""The issue-details command needs Jira issue read scopes.

{REQUIRED_SCOPE_HELP}"""
SEARCH_SCOPE_HELP = f"""The list-tickets command uses Jira enhanced JQL search.

{REQUIRED_SCOPE_HELP}"""
FIELD_SCOPE_HELP = f"""Updating custom fields needs Jira field and issue-write scopes.

{REQUIRED_SCOPE_HELP}

If field lookup fails, set this in scripts/jira/.env:
  export AI_CONTRIBUTION_FIELD_ID="customfield_12345"
  export PERCENT_DONE_FIELD_ID="customfield_67890" """


class JiraError(RuntimeError):
    pass


class QuitRequested(Exception):
    pass


def load_env_file(path: Path) -> None:
    if not path.exists():
        return

    for raw_line in path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        # if line.startswith("export "):
        #     line = line[len("export ") :].strip()
        if "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()

        if not key or not re.match(r"^[A-Za-z_][A-Za-z0-9_]*$", key):
            continue

        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]

        APP_CONFIG[key] = value


def config_value(name: str) -> str | None:
    return APP_CONFIG.get(name) or os.environ.get(name)


def require_env(name: str) -> str:
    value = config_value(name)
    if not value:
        raise JiraError(f"missing environment variable: {name}")
    return value


def normalize_site(site: str) -> str:
    site = site.removeprefix("https://").removeprefix("http://")
    return site.strip("/")


def request_json(
    method: str,
    url: str,
    *,
    body: dict[str, Any] | None = None,
    auth: bool = True,
) -> Any:
    headers = {"Accept": "application/json"}
    data = None

    if body is not None:
        data = json.dumps(body).encode()
        headers["Content-Type"] = "application/json"

    if auth:
        email = require_env("JIRA_EMAIL")
        token = require_env("JIRA_API_TOKEN")
        encoded = base64.b64encode(f"{email}:{token}".encode()).decode()
        headers["Authorization"] = f"Basic {encoded}"

    req = Request(url=url, data=data, headers=headers, method=method)

    try:
        with urlopen(req) as response:
            content = response.read().decode()
            if not content:
                return None
            return json.loads(content)
    except HTTPError as exc:
        detail = exc.read().decode(errors="replace")
        raise JiraError(f"Jira API returned HTTP {exc.code}: {detail}") from exc
    except URLError as exc:
        raise JiraError(f"request failed: {exc.reason}") from exc


def get_cloud_id() -> str:
    cloud_id = config_value("JIRA_CLOUD_ID")
    if cloud_id:
        return cloud_id

    site = normalize_site(require_env("JIRA_SITE"))
    data = request_json("GET", f"https://{site}/_edge/tenant_info", auth=False)

    try:
        return data["cloudId"]
    except (TypeError, KeyError) as exc:
        raise JiraError("could not find cloudId in tenant_info response") from exc


def jira_url(path: str) -> str:
    return f"https://api.atlassian.com/ex/jira/{get_cloud_id()}{path}"


def jira_request(method: str, path: str, body: dict[str, Any] | None = None) -> Any:
    return request_json(method, jira_url(path), body=body)


def adf_doc(text: str) -> dict[str, Any]:
    return {
        "type": "doc",
        "version": 1,
        "content": [
            {
                "type": "paragraph",
                "content": [{"type": "text", "text": text}],
            }
        ],
    }


def read_text_arg(value: str | None, empty_message: str) -> str:
    text = value if value is not None else sys.stdin.read()
    text = text.rstrip("\n")
    if not text:
        raise JiraError(empty_message)
    return text


def parse_duration_seconds(value: str) -> int:
    if re.fullmatch(r"\d+", value):
        return int(value)

    total = 0
    matched = False
    for amount, unit in re.findall(r"(\d+(?:\.\d+)?)([hm])", value.lower()):
        matched = True
        if unit == "h":
            total += int(float(amount) * 3600)
        elif unit == "m":
            total += int(float(amount) * 60)

    if matched and total > 0:
        return total

    raise JiraError("duration must be seconds, or values like 30m, 1h, 1h30m")


def parse_positive_int(value: str, label: str) -> int:
    if not re.fullmatch(r"\d+", value):
        raise JiraError(f"{label} must be a positive integer")

    parsed = int(value)
    if parsed <= 0:
        raise JiraError(f"{label} must be greater than zero")
    return parsed


def parse_percent(value: str) -> int:
    raw = value.rstrip("%")
    if not re.fullmatch(r"\d+", raw):
        raise JiraError("%Done must be an integer percentage")

    parsed = int(raw)
    if not 0 <= parsed <= 100:
        raise JiraError("%Done must be between 0 and 100")
    return parsed


def jira_started(value: str | None) -> str:
    if value is None:
        return datetime.now().astimezone().strftime("%Y-%m-%dT%H:%M:%S.000%z")

    text = value.strip()
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.000[+-]\d{4}", text):
        return text

    formats = [
        "%Y-%m-%d %H:%M",
        "%Y-%m-%d %I:%M %p",
        "%Y-%m-%dT%H:%M",
        "%Y-%m-%dT%H:%M:%S",
    ]

    for fmt in formats:
        try:
            dt = datetime.strptime(text, fmt).astimezone()
            return dt.strftime("%Y-%m-%dT%H:%M:%S.000%z")
        except ValueError:
            pass

    raise JiraError(
        "started must be like '2026-05-19 11:00' or "
        "'2026-05-19T11:00:00.000+0600'"
    )


def print_json(data: Any) -> None:
    if data is not None:
        print(json.dumps(data, indent=2, sort_keys=True))


def print_issue_table(issues: list[dict[str, Any]]) -> None:
    if not issues:
        print("No tickets found.")
        return

    rows = []
    for issue in issues:
        fields = issue.get("fields") or {}
        status = fields.get("status") or {}
        assignee = fields.get("assignee") or {}
        rows.append(
            [
                issue.get("key", ""),
                status.get("name", "Unknown"),
                assignee.get("displayName") or "Unassigned",
                (fields.get("summary") or "").replace("\n", " "),
            ]
        )

    widths = [
        max(len("Key"), *(len(row[0]) for row in rows)),
        max(len("Status"), *(len(row[1]) for row in rows)),
        max(len("Assignee"), *(len(row[2]) for row in rows)),
    ]

    print(f"{'Key':<{widths[0]}}  {'Status':<{widths[1]}}  {'Assignee':<{widths[2]}}  Summary")
    print(f"{'-' * widths[0]}  {'-' * widths[1]}  {'-' * widths[2]}  -------")
    for key, status, assignee, summary in rows:
        print(f"{key:<{widths[0]}}  {status:<{widths[1]}}  {assignee:<{widths[2]}}  {summary}")


def search_issues(jql: str, max_results: int) -> list[dict[str, Any]]:
    params = {
        "jql": jql,
        "maxResults": max_results,
        "fields": ["summary", "status", "assignee"],
    }
    path = f"/rest/api/3/search/jql?{urlencode(params, doseq=True)}"
    try:
        data = jira_request("GET", path)
    except JiraError as exc:
        if "scope does not match" in str(exc):
            raise JiraError(f"{exc}\n\n{SEARCH_SCOPE_HELP}") from exc
        raise
    return data.get("issues", [])


def build_assignee_jql(
    assignee: str,
    *,
    project: str | None = None,
    order_by: str = "updated DESC",
) -> str:
    clauses = []
    if project:
        clauses.append(f"project = {project.strip().upper()}")

    if assignee == "currentUser()":
        clauses.append("assignee = currentUser()")
    elif assignee == "EMPTY":
        clauses.append("assignee is EMPTY")
    else:
        clauses.append(f"assignee = {assignee}")

    return f"{' AND '.join(clauses)} ORDER BY {order_by}"


def find_field_id(field_name: str) -> str:
    params = {
        "type": "custom",
        "query": field_name,
        "maxResults": 50,
    }
    path = f"/rest/api/3/field/search?{urlencode(params, doseq=True)}"
    try:
        data = jira_request("GET", path)
    except JiraError as exc:
        if "scope does not match" in str(exc):
            raise JiraError(f"{exc}\n\n{FIELD_SCOPE_HELP}") from exc
        raise

    fields = data.get("values", [])
    exact_matches = [
        field for field in fields if field.get("name", "").casefold() == field_name.casefold()
    ]
    if not exact_matches:
        names = ", ".join(
            f"{field.get('name')} ({field.get('id')})" for field in fields[:10]
        )
        extra = f" Matching fields returned: {names}" if names else ""
        raise JiraError(
            f"could not find Jira field named {field_name!r}.{extra}\n\n{FIELD_SCOPE_HELP}"
        )

    return exact_matches[0]["id"]


def get_custom_field_id(
    field_name: str,
    env_var: str,
    field_id: str | None = None,
) -> str:
    if field_id:
        return field_id

    env_field_id = config_value(env_var)
    if env_field_id:
        return env_field_id

    return find_field_id(field_name)


def get_editmeta_field(issue_key: str, field_id: str) -> dict[str, Any]:
    issue = quote(issue_key, safe="")
    try:
        data = jira_request("GET", f"/rest/api/3/issue/{issue}/editmeta")
    except JiraError as exc:
        if "scope does not match" in str(exc):
            raise JiraError(f"{exc}\n\n{FIELD_SCOPE_HELP}") from exc
        raise

    fields = data.get("fields") or {}
    if field_id not in fields:
        raise JiraError(
            f"field {field_id!r} is not editable for {issue_key}. "
            "Check the ticket type, workflow status, and Jira screen configuration."
        )
    return fields[field_id]


def select_option_payload(
    issue_key: str,
    field_name: str,
    field_id: str,
    candidate_values: list[str],
) -> dict[str, str]:
    meta = get_editmeta_field(issue_key, field_id)
    allowed_values = meta.get("allowedValues") or []

    for candidate in candidate_values:
        for option in allowed_values:
            if str(option.get("value", "")).casefold() == candidate.casefold():
                return {"id": str(option["id"])}

    allowed = ", ".join(str(option.get("value")) for option in allowed_values)
    raise JiraError(
        f"{field_name} value must match one of the configured Jira options: {allowed}"
    )


def update_custom_field(
    issue_key: str,
    field_name: str,
    field_id: str,
    value: Any,
    display_value: str,
) -> None:
    issue = quote(issue_key, safe="")
    payload = {"fields": {field_id: value}}

    try:
        jira_request("PUT", f"/rest/api/3/issue/{issue}", payload)
    except JiraError as exc:
        if "scope does not match" in str(exc):
            raise JiraError(f"{exc}\n\n{FIELD_SCOPE_HELP}") from exc
        raise

    print(f"Updated {issue_key}: {field_name} = {display_value}")


def cmd_cloud_id(_: argparse.Namespace) -> None:
    print(get_cloud_id())


def cmd_check_auth(_: argparse.Namespace) -> None:
    # /myself needs user-read scopes that are not required for posting comments
    # or worklogs. serverInfo lets us verify the token and gateway URL without
    # forcing extra scopes onto the token.
    print_json(jira_request("GET", "/rest/api/3/serverInfo"))


def cmd_scopes(_: argparse.Namespace) -> None:
    print(REQUIRED_SCOPE_HELP)


def cmd_issue(args: argparse.Namespace) -> None:
    issue = quote(args.issue, safe="")
    path = f"/rest/api/3/issue/{issue}?fields=summary,status,assignee"
    try:
        print_json(jira_request("GET", path))
    except JiraError as exc:
        if "scope does not match" in str(exc):
            raise JiraError(f"{exc}\n\n{ISSUE_SCOPE_HELP}") from exc
        raise


def cmd_list_issues(args: argparse.Namespace) -> None:
    if args.max <= 0:
        raise JiraError("--max must be a positive integer")

    if args.jql:
        jql = args.jql
    else:
        if not args.project:
            raise JiraError("provide a project key or use --jql")
        project = args.project.strip().upper()
        jql = f"project = {project} ORDER BY updated DESC"

    print_issue_table(search_issues(jql, args.max))


def cmd_list_assignee(args: argparse.Namespace) -> None:
    if args.max <= 0:
        raise JiraError("--max must be a positive integer")

    selected = [bool(args.me), bool(args.account_id), bool(args.unassigned)]
    if sum(selected) != 1:
        raise JiraError("choose exactly one of --me, --account-id, or --unassigned")

    if args.me:
        assignee = "currentUser()"
    elif args.unassigned:
        assignee = "EMPTY"
    else:
        assignee = args.account_id

    jql = build_assignee_jql(assignee, project=args.project)
    print_issue_table(search_issues(jql, args.max))


def cmd_find_field(args: argparse.Namespace) -> None:
    field_name = args.name or AI_CONTRIBUTION_FIELD_NAME
    print(find_field_id(field_name))


def cmd_comment(args: argparse.Namespace) -> None:
    text = read_text_arg(args.text, "comment text is empty")
    issue = quote(args.issue, safe="")
    payload = {"body": adf_doc(text)}
    print_json(jira_request("POST", f"/rest/api/3/issue/{issue}/comment", payload))


def cmd_worklog(args: argparse.Namespace) -> None:
    text = read_text_arg(args.text, "worklog comment is empty")
    issue = quote(args.issue, safe="")
    payload = {
        "started": jira_started(args.started),
        "timeSpentSeconds": parse_duration_seconds(args.duration),
        "comment": adf_doc(text),
    }
    print_json(jira_request("POST", f"/rest/api/3/issue/{issue}/worklog", payload))


def cmd_ai_contribution(args: argparse.Namespace) -> None:
    value = parse_positive_int(args.value, "AI contribution")
    field_id = get_custom_field_id(
        AI_CONTRIBUTION_FIELD_NAME,
        "AI_CONTRIBUTION_FIELD_ID",
        args.field_id,
    )
    payload_value = select_option_payload(
        args.issue,
        AI_CONTRIBUTION_FIELD_NAME,
        field_id,
        [str(value)],
    )
    update_custom_field(
        args.issue,
        AI_CONTRIBUTION_FIELD_NAME,
        field_id,
        payload_value,
        str(value),
    )


def cmd_percent_done(args: argparse.Namespace) -> None:
    value = parse_percent(args.value)
    field_id = get_custom_field_id(
        PERCENT_DONE_FIELD_NAME,
        "PERCENT_DONE_FIELD_ID",
        args.field_id,
    )
    payload_value = select_option_payload(
        args.issue,
        PERCENT_DONE_FIELD_NAME,
        field_id,
        [f"{value}%", str(value)],
    )
    update_custom_field(
        args.issue,
        PERCENT_DONE_FIELD_NAME,
        field_id,
        payload_value,
        f"{value}%",
    )


def prompt_input(label: str) -> str:
    try:
        value = input(label)
    except EOFError as exc:
        raise QuitRequested from exc

    if value.strip().casefold() == "q":
        raise QuitRequested
    return value


def prompt_required(label: str) -> str:
    while True:
        value = prompt_input(label).strip()
        if value:
            return value
        print("Value is required.")


def prompt_choice(label: str, options: list[str]) -> int:
    while True:
        print(label)
        for idx, option in enumerate(options, start=1):
            print(f"{idx}. {option}")

        value = prompt_input("Select option: ").strip()
        if value.isdigit() and 1 <= int(value) <= len(options):
            return int(value)
        print("Invalid option. Enter q to quit.\n")


def prompt_multiline() -> str:
    print("Enter multiline comment. Finish with a line containing only EOF. Enter q to quit.")
    lines: list[str] = []
    while True:
        try:
            line = prompt_input("")
        except EOFError:
            break
        if line == "EOF":
            break
        lines.append(line)

    text = "\n".join(lines).strip()
    if not text:
        raise JiraError("comment text is empty")
    return text


def interactive_comment() -> None:
    comment_type = prompt_choice(
        "\nComment input type:",
        ["Single-line comment", "Multiline comment"],
    )
    issue = prompt_required("Ticket number, for example P1732-800: ")

    if comment_type == 1:
        text = prompt_required("Comment: ")
    else:
        text = prompt_multiline()

    args = argparse.Namespace(issue=issue, text=text)
    cmd_comment(args)


def interactive_worklog() -> None:
    issue = prompt_required("Ticket number, for example P1732-800: ")
    duration = prompt_required("Duration, for example 30m, 1h, 1h30m, or 1800: ")
    started = prompt_input(
        "Started time, for example 2026-05-19 11:00 (blank = now): "
    ).strip()

    comment_type = prompt_choice(
        "\nWorklog comment input type:",
        ["Single-line comment", "Multiline comment"],
    )
    if comment_type == 1:
        text = prompt_required("Worklog comment: ")
    else:
        text = prompt_multiline()

    args = argparse.Namespace(
        issue=issue,
        duration=duration,
        text=text,
        started=started or None,
    )
    cmd_worklog(args)


def interactive_issue() -> None:
    issue = prompt_required("Ticket number, for example P1732-800: ")
    cmd_issue(argparse.Namespace(issue=issue))


def interactive_list_issues() -> None:
    project = prompt_required("Project key, for example P1732: ")
    max_text = prompt_input("Maximum tickets to show (default 50): ").strip()
    if max_text:
        if not max_text.isdigit() or int(max_text) <= 0:
            raise JiraError("maximum tickets must be a positive integer")
        max_results = int(max_text)
    else:
        max_results = 50

    cmd_list_issues(argparse.Namespace(project=project, max=max_results, jql=None))


def interactive_list_assignee() -> None:
    assignee_type = prompt_choice(
        "\nAssignee filter:",
        ["Me", "Specific accountId", "Unassigned"],
    )
    project = prompt_input(
        "Project key, for example P1732 (blank = all visible projects): "
    ).strip()
    max_text = prompt_input("Maximum tickets to show (default 50): ").strip()
    if max_text:
        if not max_text.isdigit() or int(max_text) <= 0:
            raise JiraError("maximum tickets must be a positive integer")
        max_results = int(max_text)
    else:
        max_results = 50

    if assignee_type == 1:
        args = argparse.Namespace(
            me=True,
            account_id=None,
            unassigned=False,
            project=project or None,
            max=max_results,
        )
    elif assignee_type == 2:
        args = argparse.Namespace(
            me=False,
            account_id=prompt_required("Assignee accountId: "),
            unassigned=False,
            project=project or None,
            max=max_results,
        )
    else:
        args = argparse.Namespace(
            me=False,
            account_id=None,
            unassigned=True,
            project=project or None,
            max=max_results,
        )

    cmd_list_assignee(args)


def interactive_ai_contribution() -> None:
    issue = prompt_required("Ticket number, for example P1732-800: ")
    value = prompt_required("AI contribution positive integer: ")
    cmd_ai_contribution(argparse.Namespace(issue=issue, value=value, field_id=None))


def interactive_percent_done() -> None:
    issue = prompt_required("Ticket number, for example P1732-800: ")
    value = prompt_required("%Done value, 0 to 100: ")
    cmd_percent_done(argparse.Namespace(issue=issue, value=value, field_id=None))


def run_interactive(env_file: Path) -> int:
    load_env_file(env_file)

    while True:
        try:
            choice = prompt_choice(
                "\nJira Automation (enter q to quit)",
                [
                    "Add comment",
                    "Add worklog",
                    "List tickets",
                    "List tickets by assignee",
                    "Get issue details",
                    "Check authentication",
                    "Show Cloud ID",
                    "Show required scopes",
                    "Update AI contribution",
                    "Update %Done",
                ],
            )

            if choice == 1:
                interactive_comment()
            elif choice == 2:
                interactive_worklog()
            elif choice == 3:
                interactive_list_issues()
            elif choice == 4:
                interactive_list_assignee()
            elif choice == 5:
                interactive_issue()
            elif choice == 6:
                cmd_check_auth(argparse.Namespace())
            elif choice == 7:
                cmd_cloud_id(argparse.Namespace())
            elif choice == 8:
                cmd_scopes(argparse.Namespace())
            elif choice == 9:
                interactive_ai_contribution()
            elif choice == 10:
                interactive_percent_done()
        except JiraError as exc:
            print(f"error: {exc}", file=sys.stderr)
        except QuitRequested:
            print("\nExiting.")
            return 0

        print()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Jira Cloud helper for scoped API-token comments and worklogs.",
        epilog=HELP_EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--env-file",
        default=str(DEFAULT_ENV_FILE),
        help=f"env file to load first; default: {DEFAULT_ENV_FILE}",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    cloud_id = subparsers.add_parser("cloud-id", help="print Jira Cloud ID")
    cloud_id.set_defaults(func=cmd_cloud_id)

    check_auth = subparsers.add_parser("check-auth", help="verify credentials")
    check_auth.set_defaults(func=cmd_check_auth)

    scopes = subparsers.add_parser("scopes", help="print required Jira token scopes")
    scopes.set_defaults(func=cmd_scopes)

    issue = subparsers.add_parser("issue", help="fetch issue summary/status/assignee")
    issue.add_argument("issue", help="issue key, for example P1732-800")
    issue.set_defaults(func=cmd_issue)

    list_issues = subparsers.add_parser("list-issues", help="list tickets using JQL")
    list_issues.add_argument("project", nargs="?", help="project key, for example P1732")
    list_issues.add_argument("--max", type=int, default=50, help="maximum tickets to show")
    list_issues.add_argument(
        "--jql",
        help="custom bounded JQL, for example 'project = P1732 ORDER BY updated DESC'",
    )
    list_issues.set_defaults(func=cmd_list_issues)

    list_assignee = subparsers.add_parser(
        "list-assignee",
        help="list tickets by assignee",
    )
    assignee_group = list_assignee.add_mutually_exclusive_group(required=True)
    assignee_group.add_argument("--me", action="store_true", help="list current user's tickets")
    assignee_group.add_argument("--account-id", help="assignee accountId")
    assignee_group.add_argument("--unassigned", action="store_true", help="list unassigned tickets")
    list_assignee.add_argument("--project", help="optional project key, for example P1732")
    list_assignee.add_argument("--max", type=int, default=50, help="maximum tickets to show")
    list_assignee.set_defaults(func=cmd_list_assignee)

    find_field = subparsers.add_parser("find-field", help="find a Jira custom field ID")
    find_field.add_argument(
        "name",
        nargs="?",
        default=AI_CONTRIBUTION_FIELD_NAME,
        help=f"field name; default: {AI_CONTRIBUTION_FIELD_NAME!r}",
    )
    find_field.set_defaults(func=cmd_find_field)

    comment = subparsers.add_parser("comment", help="add a comment to an issue")
    comment.add_argument("issue", help="issue key, for example P1732-800")
    comment.add_argument("text", nargs="?", help="comment text; stdin if omitted")
    comment.set_defaults(func=cmd_comment)

    worklog = subparsers.add_parser("worklog", help="add a worklog to an issue")
    worklog.add_argument("issue", help="issue key, for example P1732-800")
    worklog.add_argument("duration", help="seconds, 30m, 1h, or 1h30m")
    worklog.add_argument("text", nargs="?", help="worklog comment; stdin if omitted")
    worklog.add_argument(
        "--started",
        help="start time, for example '2026-05-19 11:00'",
    )
    worklog.set_defaults(func=cmd_worklog)

    ai_contribution = subparsers.add_parser(
        "ai-contribution",
        help=f"update the {AI_CONTRIBUTION_FIELD_NAME!r} custom field",
    )
    ai_contribution.add_argument("issue", help="issue key, for example P1732-800")
    ai_contribution.add_argument("value", help="positive integer value")
    ai_contribution.add_argument(
        "--field-id",
        help="custom field ID, for example customfield_12345; overrides env lookup",
    )
    ai_contribution.set_defaults(func=cmd_ai_contribution)

    percent_done = subparsers.add_parser(
        "percent-done",
        help="update the '%%Done' custom field",
    )
    percent_done.add_argument("issue", help="issue key, for example P1732-800")
    percent_done.add_argument("value", help="percentage value from 0 to 100")
    percent_done.add_argument(
        "--field-id",
        help="custom field ID, for example customfield_67890; overrides env lookup",
    )
    percent_done.set_defaults(func=cmd_percent_done)

    return parser


def main() -> int:
    if len(sys.argv) == 1:
        return run_interactive(DEFAULT_ENV_FILE)

    parser = build_parser()
    args = parser.parse_args()
    load_env_file(Path(args.env_file).expanduser())

    try:
        args.func(args)
        return 0
    except JiraError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
