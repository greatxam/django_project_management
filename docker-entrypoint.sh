#!/bin/bash

# Collect static files
echo "Collecting static files"
python3 manage.py collectstatic -l --noinput

# Apply database migrations
echo "Applying database migrations"
python3 manage.py migrate

# run the app
echo "String the app"
apache2ctl -D FOREGROUND
