# Jira Python CLI

Use [../jira.py](../jira.py) to post Jira comments and worklogs from this repo.

## 1. Configure Credentials

Create a local env file:

```bash
cp scripts/jira/env.example scripts/jira/.env
```

Edit `scripts/jira/.env`:

```bash
export JIRA_EMAIL="your-email@example.com"
export JIRA_API_TOKEN="your-scoped-api-token"
export JIRA_SITE="bjit.atlassian.net"
```

Do not commit `scripts/jira/.env`. It is ignored by Git.

## 2. Verify Setup

```bash
python scripts/jira.py cloud-id
python scripts/jira.py check-auth
```

If `check-auth` fails with `401`, check the token, email, selected scopes, and `JIRA_SITE`.

## 3. Add A Comment

Single-line comment:

```bash
python scripts/jira.py comment P1732-800 "Implemented validation changes."
```

Multi-line comment:

```bash
cat <<'EOF' | python scripts/jira.py comment P1732-800
Implemented Jira automation.

Changes:
- Added Python CLI
- Added worklog support
- Added comment support
EOF
```

## 4. Add A Worklog

Add 30 minutes starting at 11:00 AM:

```bash
python scripts/jira.py worklog P1732-800 30m "Development work." --started "2026-05-19 11:00"
```

Other duration examples:

```bash
python scripts/jira.py worklog P1732-800 1800 "Development work."
python scripts/jira.py worklog P1732-800 1h "Development work."
python scripts/jira.py worklog P1732-800 1h30m "Development work."
```

If `--started` is omitted, the current local time is used.

## 5. Fetch Issue Details

```bash
python scripts/jira.py issue P1732-800
```

This command requires issue-read scopes. If your token only has comment/worklog scopes, comment and worklog commands can still work while `issue` fails.

## 6. Use A Different Env File

```bash
python scripts/jira.py --env-file /path/to/jira.env check-auth
```

