# Testing

## Strategy

- **Integration tests only** — no unit tests or complicated test suites
- Focus on testing APIs end-to-end

## Integration Tests (itests)

- Use **testcontainers** for real services (PostgreSQL, Redis, etc.)
- Keep tests minimal — optimize to cover every field in API results at least once across all tests
- One test may assert multiple fields; spread coverage so each field is exercised in at least one test

## Running Tests

```bash
just itest
```

This runs `uv run pytest`, which:

1. Starts a PostgreSQL container (postgres:18.2) via testcontainers before Django loads
2. Sets `DATABASE_URL` to the container's connection URL
3. Runs migrations against the test database
4. Executes integration tests

Requires Docker to be available.

## Testcontainers Flow

- **Local**: [conftest.py](../conftest.py) uses `pytest_configure` to start the container and set `DATABASE_URL` before Django loads
- **CI**: [scripts/run_tests.py](../scripts/run_tests.py) starts the container and sets `DATABASE_URL` before running pytest (avoids Django loading before `pytest_configure`)
- `pytest_unconfigure` stops the container after all tests complete (local only; CI wrapper stops it)
- The container is shared across the entire test session

## Structure

Tests live in [tests/](../tests/) and are organized by feature:

| Directory | Purpose |
|-----------|---------|
| `tests/blog/` | Wagtail API v2 at `/api/v2/pages/` — list and single post by slug |

## Coverage

- **Blog API** ([tests/blog/test_api.py](../tests/blog/test_api.py)): `title`, `date`, `intro`, `body`, `feed_image_thumbnail` fields
