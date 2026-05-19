#!/usr/bin/env bash
set -euo pipefail

die() {
  echo "error: $*" >&2
  exit 1
}

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || die "missing required command: $1"
}

require_env() {
  local name="$1"
  [[ -n "${!name:-}" ]] || die "missing environment variable: $name"
}

normalize_site() {
  local site="${1:-}"
  site="${site#https://}"
  site="${site#http://}"
  site="${site%%/}"
  printf '%s' "$site"
}

json_string() {
  require_cmd python
  python -c 'import json, sys; print(json.dumps(sys.stdin.read()))'
}

adf_doc_from_text() {
  local text_json
  text_json="$(json_string)"
  cat <<JSON
{
  "type": "doc",
  "version": 1,
  "content": [
    {
      "type": "paragraph",
      "content": [
        {
          "type": "text",
          "text": $text_json
        }
      ]
    }
  ]
}
JSON
}

get_cloud_id() {
  require_cmd curl
  require_cmd python

  if [[ -n "${JIRA_CLOUD_ID:-}" ]]; then
    printf '%s' "$JIRA_CLOUD_ID"
    return
  fi

  require_env JIRA_SITE
  local site
  site="$(normalize_site "$JIRA_SITE")"

  curl -fsS "https://${site}/_edge/tenant_info" |
    python -c 'import json, sys; print(json.load(sys.stdin)["cloudId"])'
}

jira_base_url() {
  local cloud_id
  cloud_id="$(get_cloud_id)"
  printf 'https://api.atlassian.com/ex/jira/%s' "$cloud_id"
}

jira_request() {
  require_env JIRA_EMAIL
  require_env JIRA_API_TOKEN
  require_cmd curl

  local method="$1"
  local path="$2"
  shift 2

  curl -fsS \
    -u "${JIRA_EMAIL}:${JIRA_API_TOKEN}" \
    -X "$method" \
    -H "Accept: application/json" \
    "$@" \
    "$(jira_base_url)${path}"
}
