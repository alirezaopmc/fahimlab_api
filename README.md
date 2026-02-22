# Ali Fahim Laboratory API

Django + Wagtail API project with PostgreSQL.

## Quick start (local development)

```bash
# 1. Install dependencies
just install

# 2. Copy environment and ensure DATABASE_URL points to local PostgreSQL
cp .env.example .env
# DATABASE_URL in .env.example matches compose.yaml (localhost:5432)

# 3. Start PostgreSQL (Docker)
just db

# 4. Run migrations
just migrate

# 5. Create admin user (first time only)
uv run python manage.py createsuperuser

# 6. Start development server
just run
```

**One-command dev workflow:**

```bash
just dev
```

This starts PostgreSQL, runs migrations, and starts the server.

## URLs

| URL | Description |
|-----|-------------|
| http://localhost:8000/api/v2/ | REST API (pages, images, documents) |
| http://localhost:8000/cms/ | Wagtail admin |
| http://localhost:8000/pages/ | Wagtail frontend (pages) |

## Blog API (for Next.js)

After creating a **Blog** index page and posts in the CMS (`/cms/`):

**Find the blog index ID:**
```bash
curl "http://localhost:8000/api/v2/pages/?type=blog.BlogIndexPage"
```

**List blog posts** (replace `3` with your blog index ID):
```bash
curl "http://localhost:8000/api/v2/pages/?type=blog.BlogPage&child_of=3&fields=title,meta,date,intro,body&order=-first_published_at"
```

**Single post by slug:**
```bash
curl "http://localhost:8000/api/v2/pages/?type=blog.BlogPage&slug=my-post-slug&fields=*,body"
```

For full API reference (pagination, filtering, search, fields), see [docs/11-wagtail-api.md](docs/11-wagtail-api.md).

## Commands

| Command | Description |
|---------|-------------|
| `just db` | Start PostgreSQL container |
| `just run` | Start development server |
| `just migrate` | Run database migrations |
| `just migrate-create` | Create new migrations |
| `just dev` | Start db, migrate, then run server |
| `just lint` | Run Ruff linter |
| `just format` | Format code with Ruff |
| `just install` | Install dependencies |

## Environment

Copy `.env.example` to `.env` for local development. Key variables:

| Variable | Description |
|----------|-------------|
| `DATABASE_URL` | PostgreSQL connection URL (default: `postgresql://fahimlab:fahimlab@localhost:5432/fahimlab`) |
| `SECRET_KEY` | Django secret key |
| `ALLOWED_HOSTS` | Comma-separated list (e.g. `localhost,127.0.0.1`) |
| `CORS_ALLOWED_ORIGINS` | Comma-separated origins for Next.js (default: `http://localhost:3000,http://127.0.0.1:3000`) |

## Structure

```
├── config/          # Django configuration
├── apps/
│   ├── core/        # Core app
│   └── blog/        # Blog (HomePage, BlogIndexPage, BlogPage)
├── docs/            # Documentation (see docs/README.md for index)
├── compose.yaml     # PostgreSQL service
├── manage.py
├── justfile
└── pyproject.toml
```
