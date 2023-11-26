import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://publisher:5555")
socket.setsockopt_string(zmq.SUBSCRIBE, "")

while True:
    message = socket.recv_string()
    print(f"Received: {message}")
