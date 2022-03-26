FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update

WORKDIR /code

COPY ./requirements.txt .

RUN pip install --default-timeout=100 -r requirements.txt

COPY . .

RUN chmod +x /code/docker-entrypoint.sh