#!/usr/bin/env python3
"""
Start PostgreSQL via testcontainers, set DATABASE_URL, then run pytest.

Used in CI where Django may load before conftest's pytest_configure runs.
Ensures DATABASE_URL is set before pytest (and Django) starts.
"""

import os
import subprocess
import sys

from testcontainers.postgres import PostgresContainer

postgres = PostgresContainer("postgres:18.2", driver=None)
postgres.start()
url = postgres.get_connection_url()
if url.startswith("postgres://"):
    url = url.replace("postgres://", "postgresql://", 1)
os.environ["DATABASE_URL"] = url

try:
    sys.exit(
        subprocess.run(
            [sys.executable, "-m", "pytest", *sys.argv[1:]],
            env=os.environ,
        ).returncode
    )
finally:
    postgres.stop()
