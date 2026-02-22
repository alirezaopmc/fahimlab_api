"""
Pytest configuration for integration tests with testcontainers.

Starts a PostgreSQL container before Django loads so DATABASE_URL points
to the container. The container is shared across the entire test session.
"""

import os

from testcontainers.postgres import PostgresContainer

_postgres_container = None


def pytest_configure(config):
    """Start PostgreSQL container and set DATABASE_URL before Django loads."""
    global _postgres_container
    _postgres_container = PostgresContainer("postgres:18.2")
    _postgres_container.start()
    url = _postgres_container.get_connection_url()
    if url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql://", 1)
    os.environ["DATABASE_URL"] = url


def pytest_unconfigure(config):
    """Stop PostgreSQL container after all tests complete."""
    global _postgres_container
    if _postgres_container is not None:
        _postgres_container.stop()
        _postgres_container = None
