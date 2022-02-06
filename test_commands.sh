#!/bin/bash

# GET /activities/
http://127.0.0.1:8000/activities

# GET /activities/{activity_id}
http://127.0.0.1:8000/activities/7

# POST /activities/
curl -X POST http://127.0.0.1:8000/activities -H 'Content-Type: application/json' -d

# DELETE /activities/{activity_id}
