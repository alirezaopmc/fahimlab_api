# Architecture

## App Layout

| App | Purpose |
|-----|---------|
| `core` | Shared utilities, base models, common logic |
| `blog` | Blog posts (Wagtail HomePage, BlogPage) |
| `people` | Lab members, Person, PersonLink, PersonPosition (planned) |
| `publications` | Publications, citations (planned) |
| `projects` | Research projects (planned) |
| `accounts` | User accounts, auth (planned) |
| `storage` | S3/media abstraction (planned) |

## Layers

1. **Domain**: Models, entities, value objects
2. **Application**: Services (`{app}/services.py`), use cases
3. **Infrastructure**: Repositories (`{app}/repositories.py`), storage adapters
4. **Interface**: Wagtail API ([config/api.py](../config/api.py)), DRF viewsets (planned)

## Repository Pattern

- Prefer Django ORM for queries
- Use `{app}/repositories.py` for data access abstraction
- If raw SQL is required, use parameterized queries; add a comment/annotation above the function explaining why raw SQL was used
