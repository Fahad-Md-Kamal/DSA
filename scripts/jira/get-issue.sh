#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/common.sh"

usage() {
  cat >&2 <<'USAGE'
Usage:
  scripts/jira/get-issue.sh ISSUE_KEY

Example:
  scripts/jira/get-issue.sh ABC-123
USAGE
  exit 2
}

[[ $# -eq 1 ]] || usage

jira_request GET "/rest/api/3/issue/$1?fields=summary,status,assignee"
printf '\n'
