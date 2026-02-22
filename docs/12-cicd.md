# CI/CD

## Overview

GitHub Actions runs tests **only when a pull request is approved**. This reduces CI usage and ensures tests run on code that has passed review.

## Workflow

- **Trigger**: `pull_request_review` with `submitted` — runs when a review is submitted
- **Condition**: `github.event.review.state == 'APPROVED'` — only runs when the review is an approval
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
