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
ARG DJANGO_SUPERUSER_PASSWORD
ARG DJANGO_SUPERUSER_EMAIL
ARG SECRET_KEY


WORKDIR /app

ADD . /app/

ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
ENV PORT=80
ENV DEBUG=${DEBUG}
ENV DB_ENGINE=${DB_ENGINE}
ENV DB_NAME=${DB_NAME}
ENV DB_USER=${DB_USER}
ENV DB_PASSWORD=${DB_PASSWORD}
ENV DB_HOST=${DB_HOST}
ENV DB_PORT=${DB_PORT}
ENV DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD}
ENV DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL}
ENV SECRET_KEY=${SECRET_KEY}}


RUN apt-get update && \
    apt-get install -f -y postgresql-client && \
    pip3 install --upgrade pip && \
    pip3 install pipenv && \
    pipenv install --skip-lock --system --dev && \
    python manage.py flush --noinput && \
    python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py collectstatic --noinput && \
    apt-get clean && \
    apt-get autoclean && \
    apt-get autoremove && \
    python manage.py createsuperuser --email ${DJANGO_SUPERUSER_EMAIL} --noinput


EXPOSE 80
CMD gunicorn agora_project.wsgi:application --bind 0.0.0.0:$PORT
RUN python manage.py loaddata fixtures/*.json