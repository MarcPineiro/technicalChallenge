# Use an official Python runtime as a parent image
FROM python:3.11.3-slim-bullseye

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y gcc default-libmysqlclient-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /django

RUN mkdir -p ./db

COPY . /django/

COPY requirements.txt /django/

#RUN apt update -y && apt install -y python3-pip python3-dev libpq-dev postgresql postgresql-contrib

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

# Expose port 80
EXPOSE 80

# Run the application
CMD ["sh", "entrypoint.sh"]
