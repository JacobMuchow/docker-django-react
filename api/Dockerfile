FROM python:2.7
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/api
ADD requirements.txt /app/api
RUN pip install -r requirements.txt
ADD . /app/api

CMD ["django-admin", "startproject", "project"]