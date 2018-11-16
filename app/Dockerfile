FROM python:3.7
ENV PYTHONUNBUFFERED 1

WORKDIR /app/app
COPY requirements.txt /app/app
RUN pip install -r requirements.txt
COPY . /app/app

WORKDIR /app/app/project
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]