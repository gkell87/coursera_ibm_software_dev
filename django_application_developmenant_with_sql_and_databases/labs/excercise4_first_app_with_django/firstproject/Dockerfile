# syntax=docker/dockerfile:1
From python:3
ENV PYTHONDONTWRITEBYTECODE = 1
ENV PYTHONUNBUFFERED = 1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirement.txt
COPY . /code/
CMD ['python', 'mangage.py', 'runserver', '0.0.0.0:8000']