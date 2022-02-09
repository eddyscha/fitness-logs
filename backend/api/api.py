from flask import Flask
from flask_restful import Api

from .endpoints.logs import LogsApi
from .endpoints.weight import WeightsApi

from db.base import Session
from db.logs import Logs

def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(LogsApi, '/logs/<date>')
    api.add_resource(WeightsApi, '/weights/<date>')

    return app
