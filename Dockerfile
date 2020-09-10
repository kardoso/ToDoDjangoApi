#Base Image
FROM python:3.8

# create and set working directory
RUN mkdir /app
WORKDIR /app

# Add current directory code to working directory
ADD . /app/

ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive 

ENV PORT=8000

# Installing OS Dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends\
    libsqlite3-dev \
    python3-setuptools \
    python3-pip \
    python3-dev \
    python3-venv \
    git \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# install environment dependencies
RUN pip install -U pip setuptools
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

# Django Migrations
RUN python manage.py migrate

# Django service
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000 