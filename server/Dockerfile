FROM python:3.7-slim

RUN apt-get update && apt-get install -y python3-dev build-essential

WORKDIR /opt/state-machines/server

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN mkdir /var/log/state-machines/

COPY . /opt/state-machines/server
