#!/bin/bash

# Attente de la disponibilité de MySQL
if [ "$DATABASE" = "mysql" ]; then
    echo "Waiting for MySQL..."
    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 1
    done
    echo "MySQL is up - executing command"
fi

# Appliquer les migrations
echo "Applying database migrations..."
python manage.py migrate

# Créer un superutilisateur si nécessaire
echo "Creating superuser..."
python manage.py add_initial_data

# Démarrer le serveur Django
exec "$@"
