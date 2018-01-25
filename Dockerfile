FROM python:3.6.4-alpine

RUN apk update && \
	apk add git \
	build-base \
	tzdata \
	postgresql-dev

RUN echo "America/Sao_Paulo" > /etc/timezone

RUN mkdir -p /medical-appointment

WORKDIR /medical-appointment

COPY ./requirements.txt /medical-appointment/

RUN pip install -r requirements.txt

ADD . /medical-appointment/

RUN alembic init migrations
