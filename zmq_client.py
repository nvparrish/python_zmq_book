#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost::5555
#   Sends "Hello" to server, expects "World" back
#

import zmq
import messages

context = zmq.Context()

# Socket to talk to server

print("Connecting to hello world server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Do 10 requests, waiting each time for a response
for request in range(10):
    print(f"Sending request {request} ...")
    socket.send(b"Hello")
    msgs = messages.s_recv_strings(socket)
    for message in msgs:
        print(f"{message}")
