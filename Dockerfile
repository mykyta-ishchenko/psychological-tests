FROM python:3.10-slim

ENV CONTAINER_HOME=/var/www

ADD . $CONTAINER_HOME
WORKDIR $CONTAINER_HOME


RUN pip install -r $CONTAINER_HOME/requirements.txt
ENTRYPOINT gunicorn --bind 0.0.0.0:8000 --workers 4 "src.main:create_app()"
