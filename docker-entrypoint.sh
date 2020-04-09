#!/bin/bash

# Collect static files
echo "Collecting static files"
python3 manage.py collectstatic -l --noinput --settings=project_management.settings_docker

# Apply database migrations
echo "Applying database migrations"
python3 manage.py migrate --settings=project_management.settings_docker

# Initialize Agile app
echo "Initializing Agile app"
python3 manage.py agile_initialize --settings=project_management.settings_docker

# run the app
echo "String the app"
apache2ctl -D FOREGROUND
