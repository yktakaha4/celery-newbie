FROM python:3.9

RUN pip install poetry

WORKDIR /tmp

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false \
    && poetry install

WORKDIR /app
