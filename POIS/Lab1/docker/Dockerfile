FROM python:3.10.7-slim-bullseye AS base 

LABEL maintainer="Alexandr Rutkovskij <kitanoyoru@protonmail.com>"

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

FROM base AS builder 

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        build-essential

ENV POETRY_VERSION=1.0.5
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

WORKDIR $PYSETUP_PATH
COPY ./poetry.lock ./pyproject.toml ./
RUN poetry install --no-dev 

FROM python-base as production
ENV FLASK_ENV=production

COPY --from=builder $VENV_PATH $VENV_PATH

COPY ./docker/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

COPY ./app /app
COPY ./main.py /app

WORKDIR /app

ENTRYPOINT /docker-entrypoint.sh $0 $@
CMD [ "python3", "main.py"]
