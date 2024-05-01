FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY poetry.lock pyproject.toml poetry.toml /usr/src/app/

RUN pip3 install poetry

COPY . .
RUN chmod +x /app/entrypoint.sh

RUN poetry install --no-root
EXPOSE 8000

RUN apt-get update
RUN apt-get install curl
RUN curl -sL https://deb.nodesource.com/setup_21.x | bash
RUN apt-get install nodejs

RUN poetry run python manage.py tailwind install && poetry run python manage.py tailwind build
RUN DEBIAN_FRONTEND=noninteractive apt-get --yes remove nodejs
RUN rm -r theme/static_src

ENTRYPOINT /app/entrypoint.sh
