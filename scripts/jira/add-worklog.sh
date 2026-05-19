#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/common.sh"

usage() {
  cat >&2 <<'USAGE'
Usage:
  scripts/jira/add-worklog.sh ISSUE_KEY TIME_SPENT_SECONDS "worklog comment" [STARTED]
  echo "worklog comment" | scripts/jira/add-worklog.sh ISSUE_KEY TIME_SPENT_SECONDS

STARTED format:
  2026-05-19T09:00:00.000+0600

Example:
  scripts/jira/add-worklog.sh ABC-123 3600 "Development work."
USAGE
  exit 2
}

[[ $# -ge 2 && $# -le 4 ]] || usage

issue_key="$1"
time_spent_seconds="$2"
comment_text="${3:-}"
started="${4:-$(date '+%Y-%m-%dT%H:%M:%S.000%z')}"

[[ "$time_spent_seconds" =~ ^[0-9]+$ ]] || die "TIME_SPENT_SECONDS must be an integer"

if [[ -z "$comment_text" ]]; then
  comment_text="$(cat)"
fi

[[ -n "$comment_text" ]] || die "worklog comment is empty"

comment="$(printf '%s' "$comment_text" | adf_doc_from_text)"

payload="$(cat <<JSON
{
  "started": "$started",
  "timeSpentSeconds": $time_spent_seconds,
  "comment": $comment
}
JSON
)"

jira_request POST "/rest/api/3/issue/${issue_key}/worklog" \
  -H "Content-Type: application/json" \
  --data "$payload"
printf '\n'
