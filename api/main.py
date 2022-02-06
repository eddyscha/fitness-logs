import json
from typing import List

from datetime import date

from fastapi import FastAPI
from pydantic import BaseModel, parse_obj_as

class Activity(BaseModel):
    id: int
    activity: str
    time: int

class Log(BaseModel):
    date: date
    activities: List[Activity]

class Logs(BaseModel):
    data: List[Log]


app = FastAPI()

@app.get("/activities")
async def get_activities():
    with open('data/activities.json') as f:
        data = json.load(f)
        logs = parse_obj_as(Logs, data)
        return logs

@app.get("/activities/{activity_id}")
async def get_activities(activity_id: int):
    with open('data/activities.json') as f:
        data = json.load(f)
        logs = parse_obj_as(Logs, data)

        for log in logs.data:
            for activity in log.activities:
                if activity.id == activity_id:
                    return activity
        
        return None

@app.post("/activities")
async def add_logs(activity: Activity):
    with open('data/activities.json', 'r') as f:
        data = json.load(f)
        logs = parse_obj_as(Logs, data)

        date_exists = False

        for log in logs.data:
            if log.date == date.today():
                date_exists = True
                log.activities.append(activity)

        if not date_exists:
            new_log = Log(date=date.today(), activity=activity)
            logs.data.append(new_log)

    with open('data/activities.json', 'w') as f:
        f.write(logs.json())

# @app.get("/weights")
# async def get_weights():
#     with open('data/weight.json') as f:
#         logs = json.load(f)
#         return logs

# @app.post("/weights")
# async def add_logs(log: Log):
#     with open('data/weights.json', 'r+') as f:
#         logs = json.load(f)