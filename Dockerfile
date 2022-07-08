FROM python:3.10-slim-buster

RUN mkdir /src
COPY ./requirements.txt /src
WORKDIR /src

RUN  apt-get update \
     && apt-get install -y gcc libpq-dev  \
     && pip install --upgrade pip setuptools wheel

RUN pip install -r requirements.txt

COPY ./src /src


# Tell uWSGI where to find your wsgi file (change this):
ENV UWSGI_WSGI_FILE=crockery/wsgi.py

# Base uWSGI configuration (you shouldn't need to change these):
ENV UWSGI_HTTP=:8001 UWSGI_MASTER=1 UWSGI_HTTP_AUTO_CHUNKED=1 UWSGI_HTTP_KEEPALIVE=1 UWSGI_LAZY_APPS=1 UWSGI_WSGI_ENV_BEHAVIOR=holy

# Number of uWSGI workers and threads per worker (customize as needed):
ENV UWSGI_WORKERS=2 UWSGI_THREADS=4

# Deny invalid hosts before they get to Django (uncomment and change to your hostname(s)):
# ENV UWSGI_ROUTE_HOST="^(?!localhost:8001$) break:400"

# Change to a non-root user
USER ${APP_USER}:${APP_USER}

CMD ["uwsgi", "--show-config"]
