FROM python:3.11.7-alpine3.19

WORKDIR /app
ADD . /app

RUN apk add gcc && \
    apk add musl-dev \
    apk add librdkafka-dev

RUN pip install --no-cache-dir -r requirements.txt

CMD export KAFKA_SERVER_IP="$(/sbin/ip route | awk '/default/ { print $3 }')"; \
    python start.py

