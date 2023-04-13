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
RUN pip install "poetry==${POETRY_VERSION}" 

WORKDIR $PYSETUP_PATH

COPY ./pyproject.toml ./

RUN poetry install --no-dev 


FROM python:3.10.7-slim-bullseye as production
ENV FLASK_ENV=production

COPY --from=builder $VENV_PATH $VENV_PATH

COPY ./app /var/app
COPY ./main.py /var/app

COPY ./docker/entrypoint.sh /var/app

WORKDIR /var/app

CMD ["./entrypoint.sh"]
