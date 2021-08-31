FROM python:3.9-slim-buster

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /src

COPY Pipfile Pipfile.lock /src/

RUN pip install --no-cache-dir pipenv==2021.5.29 && \
    pipenv install --system --dev

COPY . /code/
