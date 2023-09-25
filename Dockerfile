FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . /app

EXPOSE 9110
#
RUN pip install -r /app/requirements.txt
CMD ["./start_app.sh"]
