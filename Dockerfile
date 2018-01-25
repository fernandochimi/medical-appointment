FROM python:3.6.4-alpine

RUN apk update && \
        apk add git \
        sqlite-dev

RUN mkdir -p /medical-appointment

WORKDIR /quotes

COPY ./requirements.txt /medical-appointment/

RUN pip install -r requirements.txt

ADD . /medical-appointment/

