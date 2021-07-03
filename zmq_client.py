#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost::5555
#   Sends "Hello" to server, expects "World" back
#

import zmq

context = zmq.Context()

# Socket to talk to server

print("Connecting to hello world server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Do 10 requests, waiting each time for a response
for request in range(10):
    print(f"Sending rquest {request} ...")
    socket.send(b"Hello")

    
    option = True
    while option:
        # Get the reply.
        message = socket.recv()
        print(f"Received reply {request} [ {message} ]")
        option = socket.getsockopt(zmq.RCVMORE)


