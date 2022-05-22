FROM python:3.7.3-slim

COPY ./requirements.txt /

RUN pip install -r requirements.txt

COPY ./anapa_hak /

COPY ./init.sh /init.sh

ENV POSTGRES_DB=

ENV POSTGRES_USER=

ENV POSTGRES_PASSWORD=

ENV DB_HOST=

ENV DB_PORT=

ENV INIT_DB=

ENV RUN_MIGRATIONS=

EXPOSE 8000

#CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]

ENTRYPOINT ["/init.sh"]