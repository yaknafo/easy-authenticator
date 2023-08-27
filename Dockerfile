FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /home/app
#COPY ./pyproject.toml ./poetry.lock* ./
#
RUN pip install -r .\requirements.txt

CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "9110", "--reload"]