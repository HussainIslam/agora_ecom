# Base Image

FROM python:3.7

WORKDIR /app

ADD . /app/

ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
ENV PORT=8888


RUN apt-get update
RUN pip3 install --upgrade pip 
RUN pip3 install pipenv
RUN pipenv install --skip-lock --system --dev

EXPOSE 8888
CMD gunicorn agora_project.wsgi:application --bind 0.0.0.0:$PORT
