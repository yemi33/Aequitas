release: python manage.py migrate
web: gunicorn backend.wsgi --log-file - --pythonpath="$PWD" config.wsgi:application
worker: python ./manage.py rqworker high default low