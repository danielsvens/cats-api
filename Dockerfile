FROM tiangolo/uwsgi-nginx-flask:python3.8

# Setup environment
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Get project
COPY . /usr/src/app/cats-api

# Install requirements
WORKDIR /usr/src/app/cats-api/
RUN pip install -r requirements.txt

# Setup environment variables
ENV UWSGI_INI /usr/src/app/cats-api/uwsgi.ini
ENV LISTEN_PORT 80
