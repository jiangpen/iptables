import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('10.1.2.1', 8765)
message = b'This is the message.  It will be repeated.'


sent = sock.sendto(message, server_address)

