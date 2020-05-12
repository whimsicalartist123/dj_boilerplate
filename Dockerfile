# Pull base image
FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY Pipfile Pipfile.lock .env /code/
RUN pip install pipenv && pipenv install --system

# Set work directory
WORKDIR /code
COPY . /code/
