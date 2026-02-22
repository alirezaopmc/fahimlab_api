# Architecture

## App Layout

| App | Purpose |
|-----|---------|
| `core` | Shared utilities, base models, common logic |
| `people` | Lab members, Person, PersonLink, PersonPosition |
| `publications` | Publications, citations |
| `projects` | Research projects |
| `blog` | Blog posts (Wagtail) |
| `accounts` | User accounts, auth |
| `storage` | S3/media abstraction |

## Layers

1. **Domain**: Models, entities, value objects
2. **Application**: Services (`{app}/services.py`), use cases
3. **Infrastructure**: Repositories (`{app}/repositories.py`), storage adapters
4. **Interface**: DRF viewsets, serializers, Wagtail API

## Repository Pattern

- Prefer Django ORM for queries
- Use `{app}/repositories.py` for data access abstraction
- If raw SQL is required, use parameterized queries; add a comment/annotation above the function explaining why raw SQL was used
