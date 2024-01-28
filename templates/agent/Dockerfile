FROM python:3.11.7-alpine3.19

WORKDIR /app
ADD . /app

RUN apk add gcc && \
    apk add musl-dev \
    apk add librdkafka-dev

RUN pip install --no-cache-dir -r requirements.txt

CMD python start.py
