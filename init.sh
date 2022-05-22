#!/usr/bin/env sh

# make migrations
if [ "$RUN_MIGRATIONS" = "yes" ];
then python manage.py makemigrations && python manage.py migrate || exit 1
fi
# TODO: load initial data
if [ "$INIT_DB" = "yes" ];
then echo "todo: load sample data" || exit 1
fi
# run wsgi
python manage.py runserver 0.0.0.0:8000