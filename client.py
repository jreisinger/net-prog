#!/usr/bin/python
import socket
import sys
import argparse

parser = argparse.ArgumentParser(description='Simple network client')
parser.add_argument('--protocol', choices=['tcp','udp'], default='tcp',
                    help='L4 protocol (default: %(default)s)')
parser.add_argument('--host', required=True)
parser.add_argument('--port', required=True)
parser.add_argument('--message', default='GET / HTTP/1.1\r\n',
                    help='data to send (default: %(default)s)')
args = parser.parse_args()

# create a socket object
if args.protocol == 'tcp':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
else:
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# connect the client
if args.protocol == 'tcp':
    client.connect((args.host, int(args.port)))

# send some data
if args.protocol == 'tcp':
    client.send(args.message)
else:
    client.sendto(args.message,(args.host, int(args.port)))

# receive some data
if args.protocol == 'tcp':
    response = client.recv(4096)
else:
    response, addr = client.recvfrom(4096)

print response
