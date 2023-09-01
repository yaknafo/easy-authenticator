#!/bin/sh

# Run Alembic migrations
python run_alembic_migration.py

# Start the FastAPI application
uvicorn main:app --host 0.0.0.0 --port 9110
