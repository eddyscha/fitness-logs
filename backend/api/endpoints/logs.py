from flask import Flask, jsonify
from flask_restful import Resource, Api

from db.base import Session
from db.logs import Logs

class LogsApi(Resource):
    def get(self, date):
        session = Session()

        logs = session.query(Logs).filter(Logs.date == date).all()
        return jsonify(logs)