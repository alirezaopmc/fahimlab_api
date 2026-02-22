# Ali Fahim Laboratory API — Design & Task Workflow

## Vision

Lab Lobby API for Ali Fahim Laboratory. Public-facing portal for lab information; admins manage content via Django admin and Wagtail CMS. Frontend consumers (e.g., Next.js) consume REST and Wagtail APIs.

## Core Principles

- **Separation of concerns**: Domain → Application → Infrastructure → Interface
- **Public vs admin**: Public API is read-optimized; admin workflows are separate
- **Stateless API**: No server-side session state for public endpoints
- **Storage abstraction**: S3 keys in DB; public URLs only (no private uploads for now)

## Architecture Layers

1. **Domain**: Models, entities, value objects
2. **Application**: Services, use cases
3. **Infrastructure**: Repositories (ORM preferred; parameterized SQL if raw), storage adapters
4. **Interface**: DRF viewsets, serializers, Wagtail API

See [docs/02-architecture.md](docs/02-architecture.md) for app layout and repository pattern.

## Task Workflow

AI IDEs must follow the embedded task templates and plan structure in [docs/09-task-workflow.md](docs/09-task-workflow.md). Update relevant docs in `docs/` when a task completes.

## Project Notes

- **Package manager**: `uv` (not pip). Use `uv add`, `uv run`, etc.
- **Config**: Read from `.env` via `django-environ`. See `.env.example`.
- **Commands**: Prefer terminal commands over manual config edits — e.g., `uv add <pkg>`, `just migrate`, `just run` (see `justfile`).
- **Docs**: Update `docs/` for each task that changes architecture, API, or behavior.
- **Testing**: Integration tests only (testcontainers); see [docs/10-testing.md](docs/10-testing.md).

## Git Workflow

- **Branch naming**: `feat/area/short-description` (e.g., `feat/blog/wagtail`) or `fix/area/short-description` (e.g., `fix/auth/session-handling`)
- **Commits**: Atomic and conventional — one logical change per commit. Examples:
  - `feat(people): add Person model`
  - `fix(auth): correct session handling`
  - `docs(api): update endpoint list`

## Object Storage

S3; store keys in DB. Public URLs only for now (no private/signed uploads). Path convention documented in [docs/05-storage.md](docs/05-storage.md).

## Security

- Rate limiting (django-ratelimit, Redis backend)
- Auth: Public endpoints read-only (no auth); Admin uses session (Django admin, Wagtail)
- CORS: django-cors-headers
- Input validation: DRF serializers; file size limits in S3 module
- SQL injection: ORM preferred; repository pattern; if raw SQL, use parameterized queries with comment/annotation
- File upload: MIME validation

See [docs/06-security.md](docs/06-security.md) for details.
