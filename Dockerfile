FROM python:3.11

WORKDIR /app

COPY requirements.txt /app

RUN apt-get update && apt-get install -y python3-pip && \
    pip install --no-cache-dir -r requirements.txt


COPY . /app

EXPOSE 3000

CMD ["python", "app.py"]