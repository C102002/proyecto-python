FROM python:3.13-slim

WORKDIR /app

RUN pip install --no-cache-dir poetry

COPY . .
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-root

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]