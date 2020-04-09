#!/bin/bash

# Collect static files
echo "Collecting static files"
python3 manage.py collectstatic -l --noinput

# Apply database migrations
echo "Applying database migrations"
python3 manage.py migrate

# run the app
echo "Starting the app"
python3 manage.py runserver 0.0.0.0:8080
