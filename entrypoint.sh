#!/bin/sh

echo 'Applying migrations...'
python3 primaProject/manage.py makemigrations
python3 primaProject/manage.py migrate

echo 'Running server...'
python3 primaProject/manage.py runserver 0.0.0.0:80