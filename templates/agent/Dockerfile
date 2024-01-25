FROM python:3.11-slim-bookworm

WORKDIR /app
ADD . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "start.py"]

