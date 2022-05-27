#!/bin/bash

echo -e "********** RUNNING MIGRATIONS **********"
python3 manage.py migrate --noinput

echo -e "********** COLLECTING STATICFILES **********"
python manage.py collectstatic --no-input

if [[ "$DJANGO_DEPLOYMENT" == "1" ]]; then
	echo -e "********** STARTING PRODUCTION SERVER **********"
	gunicorn lento_backend.wsgi:application --bind 0.0.0.0:8000 --access-logfile '-'
elif [[ "$DJANGO_DEPLOYMENT" == "0" ]]; then
	echo -e "********** STARTING DEVELOPMENT SERVER **********"
	python3 manage.py runserver 0.0.0.0:8000
fi
