FROM python:3.10-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN useradd -m -u 1000 jenkins

ENV HOME=/home/jenkins

RUN poetry install --no-root

COPY . .

