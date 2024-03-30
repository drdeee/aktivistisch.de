FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY poetry.lock pyproject.toml poetry.toml /usr/src/app/

RUN pip3 install poetry

COPY . .
RUN chmod +x /app/entrypoint.sh

RUN poetry install --no-root