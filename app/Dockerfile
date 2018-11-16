FROM python:2.7
ENV PYTHONUNBUFFERED 1

WORKDIR /app/app
COPY requirements.txt /app/app
RUN pip install -r requirements.txt
COPY . /app/app