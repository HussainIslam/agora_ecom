# Base Image

FROM python:3.7

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
    python manage.py collectstatic --noinput

EXPOSE 8888
CMD gunicorn agora_project.wsgi:application --bind 0.0.0.0:$PORT
RUN python manage.py loaddata fixtures/*.json