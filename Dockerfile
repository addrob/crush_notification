FROM python:3.11.4-bullseye
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR crush_notificator
COPY requirements.txt .
RUN apt-get update \
    && apt-get -y install firebird-server
RUN pip install -r requirements.txt
COPY . .

CMD python main.py