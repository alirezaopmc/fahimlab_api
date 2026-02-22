# API

## Endpoints

To be expanded as modules are implemented. Current structure:

- **Admin**: `/admin/` — Django admin
- **REST API**: Custom REST endpoints (versioned, e.g., `/api/v1/`)
- **Wagtail API**: Wagtail headless API for blog/content

## Auth

- Public endpoints: read-only, no auth
- Admin: session
- See [docs/06-security.md](06-security.md) for auth details

## Versioning

- REST API: URL versioning (e.g., `/api/v1/people`)
- Wagtail API: follows Wagtail conventions
