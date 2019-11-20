import socket
import sys
import datetime
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('192.168.11.107', 8889)

sock.bind(server_address)

print('begin to receive\n')
while True:
    data, address = sock.recvfrom(4096)
    print(data)
