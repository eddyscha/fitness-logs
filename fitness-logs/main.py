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

@app.get("/weights")
async def get_weights():
    with open('data/weight.json') as f:
        logs = json.load(f)
        return logs

@app.post("/activities/add")
async def add_logs(log: Log):
    with open('data/activities.json', 'r+') as f:
        logs = json.load(f)

@app.post("/weights/add")
async def add_logs(log: Log):
    with open('data/weights.json', 'r+') as f:
        logs = json.load(f)