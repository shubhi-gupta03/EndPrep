#!/bin/bash

# Deployment script for EZSem Django project

echo "Starting deployment process..."

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Run migrations
echo "Running database migrations..."
python manage.py migrate

# Create superuser if needed (uncomment if you want to create one)
# echo "Creating superuser..."
# python manage.py createsuperuser

echo "Deployment preparation complete!"
echo "Your project is ready for deployment." 