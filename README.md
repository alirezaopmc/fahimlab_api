# Ali Fahim Laboratory API

Django API project with modular structure, uv, Ruff, django-environ, and Just.

## Setup

```bash
# Install dependencies (uses uv)
just install

# Copy environment for local development (SQLite)
cp .env.development.example .env

# For production, use .env.production.example as reference and set env vars accordingly

# Run migrations
just migrate

# Start development server
just run
```

## Commands (Just)

| Command | Description |
|---------|-------------|
| `just run` | Start development server |
| `just migrate` | Run database migrations |
| `just migrate-create` | Create new migrations |
| `just lint` | Run Ruff linter |
| `just format` | Format code with Ruff |
| `just install` | Install dependencies with uv |
| `just new-app <name>` | Create new app in `apps/` |

## Environment

| File | Use case |
|------|----------|
| `.env.development.example` | Local development (SQLite) — copy to `.env` |
| `.env.production.example` | Production (PostgreSQL) — reference for deployment |

## Structure

```
├── config/          # Django configuration (settings, urls, wsgi, asgi)
├── apps/            # Business logic applications
│   └── core/        # Core app
├── manage.py
├── justfile
└── pyproject.toml
```
