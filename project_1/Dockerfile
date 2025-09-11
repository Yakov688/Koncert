FROM python:3.12-alpine


RUN pip install --upgrade pip

WORKDIR /service
COPY requirements.txt /service
COPY service /service
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r requirements.txt

RUN adduser --disabled-password service-user


USER service-user
