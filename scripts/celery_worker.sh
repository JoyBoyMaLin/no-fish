#!/bin/sh

cd /fish || exit

celery -A config worker --loglevel=info