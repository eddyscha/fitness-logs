from flask import Flask
from flask_restful import Resource, Api


def create_app():
    app = Flask(__name__)
    return app