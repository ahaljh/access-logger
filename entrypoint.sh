#!/usr/bin/env bash

python3 /code/manage.py migrate

if [ "$DEBUG" == "1" ]
then
    echo 'debug mode'
    python3 /code/manage.py runserver 0:8000
else
    echo 'production mode'
    cd /code
    gunicorn --bind 0.0.0.0:8000 accesslogger.wsgi:application
fi