FROM python:3.10

WORKDIR /app

COPY . .

CMD python3 generator.py