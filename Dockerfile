 FROM python:3.12.0
 WORKDIR /app
 COPY . /app
 CMD python inventory.py