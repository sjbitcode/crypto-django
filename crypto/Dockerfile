FROM python:3.6.4-alpine

LABEL maintainer sjbitcode@gmail.com

ENV PYTHONUNBUFFERED="TRUE" APP_PATH="/app"

# Make app directories
RUN mkdir -p $APP_PATH
WORKDIR $APP_PATH

COPY requirements.txt $APP_PATH

# Install requirements.txt
RUN pip install -r requirements.txt

ADD . $APP_PATH
