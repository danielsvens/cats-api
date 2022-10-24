# Flask API Cats

- exposes a REST API at /v1/cats/*

- provides a Dockerfile for creating a container image
- provides an uwsgi.ini file

## Run application

Application is developed on python 3.10 but should run on anything > 3.6. (hopefully :D)

```
pip install -r requirements.txt
python applicatgion.py
```

The main entrypoint is `cats/__init__.py`. It initializes the flask app, and sets up the DB.

### Migrations

Use this commands to connect and upgrade DB and initialize the schema.

```
set FLASK_APP=application.py
flask db init
flask db migrate
flask db upgrade
```
