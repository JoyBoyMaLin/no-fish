#!/bin/sh

celery -A config beat --loglevel=info --pidfile=/fish/celerybeat.pid
