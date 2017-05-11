#!/usr/bin/python
# Simple UDP client - Black Hat Python, Ch. 2

import sys
import socket

target_host = sys.argv[1]
target_port = int( sys.argv[2] )

client = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
client.sendto( "Hello", ( target_host, target_port ) )
data, addr = client.recvfrom(4096)

print data
