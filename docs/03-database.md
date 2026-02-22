# Database

## Models

### Blog (Wagtail)

| Model | Purpose |
|-------|---------|
| HomePage | Root page; only BlogIndexPage can be created under it |
| BlogIndexPage | Blog index; lists posts |
| BlogPage | Individual blog post (date, intro, body, feed_image) |

**Hierarchy:** HomePage → BlogIndexPage → BlogPage

### Planned

| Model | Purpose |
|-------|---------|
| Person | Lab member profile |
| PersonLink | External links (ORCID, Google Scholar, etc.) |
| PersonPosition | Role/position within lab |
| Publication | Research publication |
| Project | Research project |
| Apply | Application/contact form submission |

## ERD

To be expanded as models are implemented. See migrations in each app for schema.

## Migrations

- `just migrate` — Apply migrations
- `just migrate-create` — Generate new migrations
- Keep migrations small and focused
