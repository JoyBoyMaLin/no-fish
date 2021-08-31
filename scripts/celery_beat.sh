#!/bin/sh

celery -A config beat --loglevel=info --pidfile=/contract-proxy/celerybeat.pid
