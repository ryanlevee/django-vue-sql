release: python manage.py migrate --noinput
# web: gunicorn play2learn.wsgi --preload
# web: run-program waitress-serve --port=$PORT play2learn.wsgi:application
# waitress-serve --listen=127.0.0.1:8000 play2learn.wsgi:application
web: heroku ps:scale web=1