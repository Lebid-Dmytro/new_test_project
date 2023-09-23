FROM python:3.9-alpine3.16


COPY requirements.txt /main_app/requirements.txt
COPY . /main_app/
WORKDIR /main_app
EXPOSE 8000


RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r requirements.txt

RUN adduser --disabled-password main_app-user

USER main_app-user

