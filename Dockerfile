FROM python:3.11
LABEL authors="eldiyar"
ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
WORKDIR /english_backend

COPY requirements.txt /english_backend

RUN pip install --upgrade pip
RUN pip install -r /english_backend/requirements.txt
COPY . /english_backend