FROM python:3.9-slim-buster

WORKDIR /src

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PATH="${PATH}:/home/appuser/.local/bin"
ENV USER="appuser"

RUN apt-get -y update \
    && apt-get install -y curl \
    && curl -fsSL https://deb.nodesource.com/setup_14.x | bash - \
    && apt-get install -y nodejs --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && useradd --create-home appuser \
    && chown appuser:appuser -R /src

USER appuser

COPY --chown=appuser:appuser Pipfile Pipfile.lock /src/

RUN pip install --no-cache-dir pipenv==2021.5.29 && \
    pipenv install --python 3.9 --dev

COPY --chown=appuser:appuser . /src/

