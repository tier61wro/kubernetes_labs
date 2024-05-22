FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN http_proxy= https_proxy= pip3 install -r requirements.txt
# Install packages without proxy. Deletes current proxy settings on server/locally when building

COPY . .

CMD [ "python3", "app.py"]