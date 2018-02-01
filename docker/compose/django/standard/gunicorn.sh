#!/bin/sh

# /usr/bin/python3 /app/manage.py migrate
# /usr/bin/python3 /app/manage.py runscript create_admin
# /usr/bin/python3 /app/manage.py collectstatic --noinput

/usr/bin/supervisord -n -c /etc/supervisord.conf