#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/common.sh"

usage() {
  cat >&2 <<'USAGE'
Usage:
  scripts/jira/add-comment.sh ISSUE_KEY "comment text"
  echo "comment text" | scripts/jira/add-comment.sh ISSUE_KEY

Example:
  scripts/jira/add-comment.sh ABC-123 "Implemented validation and pushed updates."
USAGE
  exit 2
}

[[ $# -ge 1 && $# -le 2 ]] || usage

issue_key="$1"
comment_text="${2:-}"

if [[ -z "$comment_text" ]]; then
  comment_text="$(cat)"
fi

[[ -n "$comment_text" ]] || die "comment text is empty"

body="$(printf '%s' "$comment_text" | adf_doc_from_text)"

payload="$(cat <<JSON
{
  "body": $body
}
JSON
)"

jira_request POST "/rest/api/3/issue/${issue_key}/comment" \
  -H "Content-Type: application/json" \
  --data "$payload"
printf '\n'
