import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

while True:
    message = "Hello from PUB!"
    print(f"Publishing: {message}")
    socket.send_string(message)
    time.sleep(1)
