import os
import time
import grpc
import consumption_data_pb2
import consumption_data_pb2_grpc

def run():
    with grpc.insecure_channel("localhost:9999") as channel:
        stub = consumption_data_pb2_grpc.ConsumptionDataServiceStub(channel)
        response = stub.ConsumptionData(consumption_data_pb2.RequestData())
        for item in response.data:
            print(item.date,item.consumption)
        channel.unsubscribe(close)
        exit()


def close(channel):    
    channel.close()

if __name__ == "__main__":
    run()