#!/bin/bash

# Activate the virtual environment
source /home/f0-bg-removal/venv/bin/activate

# Navigate to your project directory
cd /home/f0-bg-removal

# Start Gunicorn with 3 workers
exec gunicorn --workers 3 --bind 127.0.0.1:8000 app:app
