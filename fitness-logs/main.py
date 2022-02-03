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

@app.get("/")
async def get_logs():
    with open('logs.json') as f:
        logs = json.load(f)
        m = parse_obj_as(Logs, logs)
        return m

@app.post("/add/")
async def add_logs(log: Log):
    with open('logs.json', 'r+') as f:
        logs = json.load(f)
        m = parse_obj_as(Logs, logs)

