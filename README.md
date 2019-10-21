A simple grpc based microservice.

## Constructions
```
# Install dependencies
pip3 install -r requirements.txt

# Generate gRPC code
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. consumption_data.proto

# Run the server
python3 server.py

# Run the client
export FLASK_APP=client.py
flask run

# Open the index.html file
