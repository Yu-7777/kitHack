FROM python:3.11

WORKDIR /app

COPY requirements.txt /app

RUN python -m ensurepip --upgrade && \
    python -m pip install --no-cache-dir -r requirements.txt


COPY . /app

EXPOSE 3000

CMD ["python", "app.py"]