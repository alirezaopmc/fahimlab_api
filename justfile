# Ali Fahim Laboratory API - Task runner
# Usage: just <recipe>

set dotenv-load

# Default
default:
    just run

# Run development server
port := env('PORT', '8000')

# Start PostgreSQL (Docker Compose)
db:
    docker compose up -d db

# Alias for db
up: db

# Full dev workflow: start db, migrate, run server
dev: db
    #!/usr/bin/env bash
    echo "Waiting for PostgreSQL..."
    sleep 3
    just migrate
    just run

run:
    uv run python manage.py runserver 0.0.0.0:{{port}}

# Run migrations
migrate:
    uv run python manage.py migrate

# Create new migrations
migrate-create:
    uv run python manage.py makemigrations

# Lint and format
lint:
    uv run ruff check .

format:
    uv run ruff format .

format-check:
    uv run ruff format --check

# Install dependencies
install:
    uv sync
