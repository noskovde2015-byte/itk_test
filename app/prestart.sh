#!/bin/sh

set -e

echo "Start Migration..."

alembic upgrade head

echo "Migration applied"

exec "$@"