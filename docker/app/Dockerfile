FROM python:3.4.3

WORKDIR /tmp
COPY requirements.txt /tmp/
RUN pip install -r requirements.txt

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
