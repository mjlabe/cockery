FROM python:3.10-slim-buster

RUN mkdir /src
COPY ./requirements.txt /src
WORKDIR /src

RUN  apt-get update \
     && apt-get install -y gcc libpq-dev  \
     && pip install --upgrade pip setuptools wheel

RUN pip install -r requirements.txt

COPY ./src /src

CMD ["uwsgi", "--show-config"]
