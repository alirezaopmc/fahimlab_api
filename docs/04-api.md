# API

## Endpoints

| URL | Description |
|-----|-------------|
| `/admin/` | Django admin |
| `/cms/` | Wagtail CMS admin |
| `/api/v2/` | Wagtail API v2 (pages, images, documents) |
| `/pages/` | Wagtail frontend (page serving) |

## Wagtail API v2

The primary public API is Wagtail's built-in REST API at `/api/v2/`. It provides read-only JSON access to:

- **Pages** — `/api/v2/pages/` (blog posts, index pages, etc.)
- **Images** — `/api/v2/images/`
- **Documents** — `/api/v2/documents/`

For full usage (pagination, filtering, fields, search, curl examples), see [docs/11-wagtail-api.md](11-wagtail-api.md).

## Auth

- **Public API** (`/api/v2/`): Read-only, no auth
- **Admin** (`/admin/`, `/cms/`): Session-based
- See [docs/06-security.md](06-security.md) for auth details

## Versioning

- Wagtail API: v2 at `/api/v2/`
- Custom REST API: Not yet implemented (future `/api/v1/` if needed)
