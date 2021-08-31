#!/bin/sh

python manage.py migrate

gunicorn -b 0.0.0.0:8000 --workers=2 --threads=4 --log-level=info --worker-class=gthread config.wsgi
