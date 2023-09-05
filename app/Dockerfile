# pull official base image
FROM python:3.10

# set work directory
WORKDIR /usr/src/NZA

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies using apt
RUN apt update \
    && apt install -y postgresql-server-dev-all gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ../requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY ../.. .
