#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter02/udp_local.py
# UDP client and server on localhost

import argparse, socket
from datetime import datetime

# The greatest length that a UDP datagram can have
MAX_BYTES = 65535

def server(port):
    sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
    # '' defaults to 0.0.0.0 (wildcard address)
    sock.bind(( '127.0.0.1', port ))
    print( 'Listening at {}'.format(sock.getsockname()) )
    while True:
        # recvfrom() waits forever until a client sends a message
        data, address = sock.recvfrom(MAX_BYTES)
        # convert bytes to string
        text = data.decode('ascii')
        print( 'The client at {} says {!r}'.format(address, text) )
        text = 'Your data was {} bytes long'.format(len(data))
        data = text.encode('ascii')
        sock.sendto(data, address)

def client(port):
    sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
    text = 'The time is {}'.format( datetime.now() )
    data = text.encode('ascii')
    # send data to address - that's it!
    sock.sendto( data, ('127.0.0.1', port) )
    print( 'The OS assgigned me the address {}'.format( sock.getsockname() ) )
    # 'Promiscuous client' - accepts every packet it sees! To prevent this:
    #   a) verify sender address after each recvfrom()
    #   b) use connect() and send()/recv() (only one server at a time)
    data, address = sock.recvfrom(MAX_BYTES)
    text = data.decode('ascii')
    print( 'The server {} replied {!r}'.format(address, text) )

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive UDP locally')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='UDP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)
