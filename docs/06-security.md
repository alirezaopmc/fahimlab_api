# Security

## Rate Limiting

- Use django-ratelimit (Redis backend)
- Apply to public and admin endpoints as appropriate

## Authentication

- **Public endpoints**: Read-only, no auth
- **Admin**: Session-based (Django admin, Wagtail)
- Configure via django-environ

## CORS

- django-cors-headers
- Restrict allowed origins in production

## Input Validation

- Use DRF serializers for request validation (for best Django compatibility)
- Pydantic can be used for advanced validation or when integrating with FastAPI
- File size limits in S3/storage module

## SQL Injection

- Prefer Django ORM
- Repository pattern for data access
- If raw SQL is required, use parameterized queries only; add comment/annotation above the function

## File Upload

- Basic security only — admins are trusted
- Validate file size (prevent accidental large uploads)
- MIME type validation required

