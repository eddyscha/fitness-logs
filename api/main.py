import json
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, parse_obj_as


class Activity(BaseModel):
    activity: str
    time: int

class Log(BaseModel):
    date: str
    activities: List[Activity]

class Logs(BaseModel):
    logs: List[Log]


app = FastAPI()

@app.get("/activities")
async def get_activities():
    with open('data/activities.json') as f:
        logs = json.load(f)
        return logs

@app.get("/activities/{activity_id}")
async def get_activities(activity_id):
    with open('data/activities.json') as f:
        logs = json.load(f)
        activity = logs["data"].get(activity_id)
        return logs

@app.post("/activities")
async def add_logs(log: Log):
    with open('data/activities.json', 'r+') as f:
        logs = json.load(f)

@app.get("/weights")
async def get_weights():
    with open('data/weight.json') as f:
        logs = json.load(f)
        return logs

@app.post("/weights")
async def add_logs(log: Log):
    with open('data/weights.json', 'r+') as f:
        logs = json.load(f)