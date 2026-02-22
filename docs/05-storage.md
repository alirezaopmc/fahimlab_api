# Storage

## Wagtail Media (images, documents)

- Currently uses local `MEDIA_ROOT`. For production, configure S3 via `django-storages` and Django's `STORAGES["default"]`.
- See [Wagtail: Storing and serving](https://docs.wagtail.org/en/stable/advanced_topics/documents/storing_and_serving.html).
- Path convention: Wagtail uses `images/` and `documents/` subdirectories under media root.

## Object Storage (S3)

- Store S3 keys in DB; generate public URLs on read
- No private/signed uploads for now — public URLs only

## Path Convention

- Use consistent path prefixes per content type (e.g., `people/{id}/`, `publications/{id}/`, `blog/{id}/`)
- Document path conventions in this doc as modules are added

## File Size

- Enforce file size limits in the storage module
- See [docs/06-security.md](06-security.md) for MIME validation
