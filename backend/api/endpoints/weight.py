from flask import Flask, jsonify
from flask_restful import Resource, Api

from db.base import Session
from db.weight import Weight

class LogsApi(Resource):
    def get(self, date):
        session = Session()
        logs = session.query(Weight).filter(Weight.date == date).all()
        session.close()

        return jsonify(logs)
