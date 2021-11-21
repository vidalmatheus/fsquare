#!/bin/bash
./manage.py collectstatic --noinput
./manage.py migrate --noinput
cd /app
DJANGO_DEBUG=1 ./manage.py runserver 0.0.0.0:8000 &
cd /app/frontend
NODE_ENV=development HOST=0.0.0.0 npm run dev &
NODE_ENV=development HOST=0.0.0.0 BASE_URL=http://localhost:8000 npm run dev:disable-mock
