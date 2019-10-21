from concurrent import futures
import threading
import time
import grpc
import consumption_data_pb2
import consumption_data_pb2_grpc
import csv

class Listener(consumption_data_pb2_grpc.ConsumptionDataServiceServicer):

    def ConsumptionData(self, request, context):
        data = []
        firstline = True
        with open('meterusage.csv', 'r') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                if firstline:    #skip first line of csv
                    firstline = False
                    continue
                data.append({"date":row[0],"consumption":row[1]})

        return consumption_data_pb2.ReturnData(data=data)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    consumption_data_pb2_grpc.add_ConsumptionDataServiceServicer_to_server(Listener(), server)
    server.add_insecure_port("[::]:9999")
    server.start()
    try:
        while True:
            print("Server Running...")
            time.sleep(10)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()