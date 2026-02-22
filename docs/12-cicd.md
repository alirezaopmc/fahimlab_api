# CI/CD

## Overview

GitHub Actions runs tests on every pull request: when the PR is opened and when new commits are pushed.

## Workflow

- **Trigger**: `pull_request` with `opened` and `synchronize` — runs on PR creation and on each push to the PR branch
- **Job**: Runs integration tests via `uv run pytest` (same as `just itest` locally)

## Success Criteria

- Pipeline **succeeds** when all tests pass
- Pipeline **fails** when any test fails

## Local Equivalence

The CI job mirrors local testing:

```bash
just itest
```

Both use testcontainers (PostgreSQL) and pytest. Docker must be available (GitHub-hosted runners have it pre-installed).

## Configuration

Workflow file: [.github/workflows/test.yml](../.github/workflows/test.yml)
