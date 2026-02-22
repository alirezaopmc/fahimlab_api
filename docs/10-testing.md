# Testing

## Strategy

- **Integration tests only** — no unit tests or complicated test suites
- Focus on testing APIs end-to-end

## Integration Tests (itests)

- Use **testcontainers** for real services (PostgreSQL, Redis, etc.)
- Keep tests minimal — optimize to cover every field in API results at least once across all tests
- One test may assert multiple fields; spread coverage so each field is exercised in at least one test

## Running Tests

- To be expanded when test setup is implemented (e.g., `just itest`)
