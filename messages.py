#
# Messages example code following the ZeroMQ
#

import zmq


def s_send_string(socket: zmq.Socket, message: bytes):
    """
    This function will call send on the socket sending the provided
    message.  Follows the ZeroMQ book.
    :param socket: The socket to use
    :param message: The message to send
    :raises TypeError: If a unicode object is passed
    :raises ValueError: If track=True but an untracked Frame is passed
    :raises ZMQError: If the send does not succeed for any reason (including if
            NOBLOCK is set and an outgoing queue is full)
    """
    flags = 0
    socket.send(message, flags)


def s_recv_string(socket: zmq.Socket):
    """
    This function will call receive on the socket and it returns
    the result.  Follows the ZeroMQ book.
    :param socket: The socket to use
    :return: The response from the socket
    :raises ZMQError: for any reasons zmq_msg_recv might fail (including if
            NOBLOCK is set and no new messages have arrived)
    """
    flags = 0
    message = socket.recv(flags)
    return message


def s_send_strings(socket: zmq.Socket, messages):
    """
    This function sends multiple strings.  Follows the ZermoMQ book.
    :param socket: The socket to use for the connection
    :param messages: A list of bytes messages to send
    :raises TypeError: If a unicode object is passed
    :raises ValueError: If track=True but an untracked Frame is passed
    :raises ZMQError: If the send does not succeed for any reason (including if
            NOBLOCK is set and an outgoing queue is full)
    """
    flags = zmq.SNDMORE
    for i, message in enumerate(messages):
        if i == len(messages) - 1:
            flags = 0
        socket.send(message, flags)

def s_recv_strings(socket: zmq.Socket):
    """
    This function receives multiple strings.  Follows the ZeroMQ book.
    :param socket: The socket to use for the connection
    :return: A list of bytes objects that were received
    :raises ZMQError: for any reasons zmq_msg_recv might fail (including if
            NOBLOCK is set and no new messages have arrived)
    """
    option = True
    messages = []
    while option:
        # Get the reply.
        messages.append(socket.recv())
        option = socket.getsockopt(zmq.RCVMORE)
    return messages
