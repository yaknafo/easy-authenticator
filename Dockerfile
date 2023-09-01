FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . /app
#
RUN pip install -r /app/requirements.txt
CMD ["./start_app.sh"]
