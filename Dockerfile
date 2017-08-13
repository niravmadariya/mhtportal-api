FROM python:3.6.2
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -U pip
RUN pip install -r requirements.txt