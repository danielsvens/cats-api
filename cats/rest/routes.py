
from flask import jsonify, request
from urllib.parse import urlparse
from datetime import datetime
from sqlalchemy.exc import IntegrityError

from .. import app
from ..model.models import Cat
from ..application.cats import CatService
from ..domain.cats import ErrorMessage

BASE_ROUTE = '/v1/cats'
CREATE_ROUTE = f'{BASE_ROUTE}/create'
LIST_ROUTE = f'{BASE_ROUTE}/list'

cat_service = CatService()

@app.route(CREATE_ROUTE, methods=['POST'])
def create():
    cat: Cat = cat_service.save_cat(request.get_json())
    return jsonify(cat), 200

@app.route(LIST_ROUTE, methods=['GET'])
def list():
    return jsonify(cat_service.get_cats()), 200

@app.errorhandler(404)
def page_not_found(e):
    path = urlparse(request.base_url).path
    return jsonify(ErrorMessage(
        timestamp=datetime.now(),
        status=404,
        error='Not Found',
        message="Endpoint doesn't exist",
        path=path
    )), 404

@app.errorhandler(TypeError)
def bad_request(e: TypeError):
    path = urlparse(request.base_url).path
    return jsonify(ErrorMessage(
        timestamp=datetime.now(),
        status=400,
        error='Bad request',
        message='Malformed request',
        path=path
    )), 400

@app.errorhandler(IntegrityError)
def bad_request(e: TypeError):
    path = urlparse(request.base_url).path
    return jsonify(ErrorMessage(
        timestamp=datetime.now(),
        status=400,
        error='Duplicate entry',
        message='Name must be unique',
        path=path
    )), 400

@app.errorhandler(405)
def internal_error(e):
    path = urlparse(request.base_url).path
    error, message = str(e).split(':')
    return jsonify(ErrorMessage(
        timestamp=datetime.now(),
        status=405,
        error='Method not allowed',
        message='The method is not allowed for the requested URL.',
        path=path
    )), 500

@app.errorhandler(500)
def internal_error(e):
    path = urlparse(request.base_url).path
    error, message = str(e).split(':')
    return jsonify(ErrorMessage(
        timestamp=datetime.now(),
        status=500,
        error=error.strip(),
        message=message.strip(),
        path=path
    )), 500
