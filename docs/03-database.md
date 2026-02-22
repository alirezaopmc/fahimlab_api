# Database

## Models (Planned)

| Model | Purpose |
|-------|---------|
| Person | Lab member profile |
| PersonLink | External links (ORCID, Google Scholar, etc.) |
| PersonPosition | Role/position within lab |
| Publication | Research publication |
| Project | Research project |
| Apply | Application/contact form submission |
| Blog | Blog posts (Wagtail) |

## ERD

To be expanded as models are implemented. See migrations in each app for schema.

## Migrations

- Use `just migrate-create` to generate migrations
- Use `just migrate` to apply migrations
- Keep migrations small and focused
