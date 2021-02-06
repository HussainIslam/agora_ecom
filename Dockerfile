# Base Image

FROM python:3.7-slim-buster

# Arguments
ARG DEBUG
ARG DB_ENGINE
ARG DB_NAME
ARG DB_USER
ARG DB_PASSWORD
ARG DB_HOST
ARG DB_PORT

WORKDIR /app

ADD . /app/

ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
ENV PORT=8888


RUN apt-get update && \
    pip3 install --upgrade pip && \
    pip3 install pipenv && \
    pipenv install --skip-lock --system --dev && \
    python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py collectstatic --noinput && \
    apt-get clean && \
    apt-get autoclean && \
    apt-get autoremove

EXPOSE 8888
CMD gunicorn agora_project.wsgi:application --bind 0.0.0.0:$PORT
RUN python manage.py loaddata fixtures/*.json