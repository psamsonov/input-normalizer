from flask import Flask, request
from models import Response, Data
import json
from flask import jsonify
import time
from datetime import datetime

app = Flask(__name__)

epoch = datetime.utcfromtimestamp(0)

def convert_date_string_to_int(input: str):
    try:
        return int((datetime.strptime(input, '%Y-%m-%dT%H:%M:%S') - epoch).total_seconds() * 1000)
    except:
        return int(float(input) * 1000)

@app.route("/")
def home():
    return "Please POST inputs to /input to receive normalized results"


@app.route("/input", methods=['POST'])
def normalize_input():
    data = json.loads(request.data)
    response = Response()
    response.source = data["deviceId"]
    response.timestamp = convert_date_string_to_int(data["timestamp"])
    response.data = dict()

    for key in data:
        if key == "deviceId" or key == "timestamp":
            continue
        response_data = Data()
        try:
            response_data.string = str(data[key])
        except:
            response_data.string = None
        try:
            response_data.numeric = float(data[key])
        except:
            response_data.numeric = None
        try:
            response_data.datetime = convert_date_string_to_int(data[key])
        except:
            response_data.datetime = None
        
        response.data[key] = response_data

    return response.toJSON()


