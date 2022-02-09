from flask import Flask, jsonify
from flask_restful import Resource, Api

from .endpoints.logs import LogsApi

from db.base import Session
from db.logs import Logs

def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(LogsApi, '/logs/<date>')

    return app
