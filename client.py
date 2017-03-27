#!/usr/bin/python
# Simple TCP client
# Usage: $0 localhost 8080 "GET / HTTP/1.1\r\n"
import socket
import sys

target_host = sys.argv[1]
target_port = int(sys.argv[2])
send_data   = sys.argv[3]

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
client.send(send_data)

# receive some data
response = client.recv(4096)

print response
