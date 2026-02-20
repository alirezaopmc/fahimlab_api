# Ali Fahim Laboratory API - Task runner
# Usage: just <recipe>

set dotenv-load

# Run development server
port := env_var_or_default('PORT', '8000')
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

