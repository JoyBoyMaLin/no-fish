#!/bin/sh

cd /contract-proxy || exit

celery -A config worker --loglevel=info