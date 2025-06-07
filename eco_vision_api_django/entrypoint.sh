#!/bin/sh

if [ ! -f "/app/db.sqlite3" ]; then
  echo "No database found, running makemigrations and migrate..."
  python manage.py makemigrations --noinput
  python manage.py migrate --noinput
else
  echo "Database already exists, skipping migration."
fi

python manage.py runserver 0.0.0.0:8000
