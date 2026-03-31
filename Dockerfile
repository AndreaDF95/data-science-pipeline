FROM python:3.11-slim

WORKDIR /app

# copia tutto
COPY . .

# installa poetry
RUN pip install poetry

# installa dipendenze
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# comando default (runner)
CMD ["python", "-m", "src.jobs.run_pipeline"]