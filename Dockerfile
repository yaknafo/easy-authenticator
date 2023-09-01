FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . /app
#
RUN pip install -r /app/requirements.txt
CMD ["python", "alembic/run_alembic_migration.py"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9110"]