FROM python:3.7.3-slim

COPY ./requirements.txt /

RUN pip install -r requirements.txt

COPY ./anapa_hak /

ENV DB_NAME="${POSTGRES_DB}"

ENV POSTGRES_USER=

ENV POSTGRES_PASSWORD=

ENV DB_HOST=

ENV DB_PORT=