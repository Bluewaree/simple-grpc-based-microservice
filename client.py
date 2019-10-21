import os
import time
import grpc
import consumption_data_pb2
import consumption_data_pb2_grpc
from flask import Flask
from google.protobuf.json_format import MessageToJson 
app = Flask(__name__)
 
@app.route('/', methods=["GET"])
def index():
    response = run()
    return MessageToJson(response)

def run():
    with grpc.insecure_channel("localhost:9999") as channel:
        stub = consumption_data_pb2_grpc.ConsumptionDataServiceStub(channel)
        response = stub.ConsumptionData(consumption_data_pb2.RequestData())
        channel.unsubscribe(close)
        return response


def close(channel):    
    channel.close()