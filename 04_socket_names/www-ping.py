#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter04/www_ping.py
# Find the WWW service of an arbitrary host using getaddrinfo().

import argparse, socket, sys

def connect_to(hostname_or_ip):
    """General way of getting info about the host/port. Ex. you don't need to
    specify IP as a protocol or TCP as a transport. All necessary info will be
    supplied by getaddrinfo()."""

    # Get info needed to connect ...
    try:
        infolist = socket.getaddrinfo(
            hostname_or_ip, 'www', 0, socket.SOCK_STREAM, 0,
            socket.AI_ADDRCONFIG | socket.AI_V4MAPPED | socket.AI_CANONNAME
            )
    # specific name service error
    except socket.gaierror as e:
        print("Name service failure:", e.args[1])
        sys.exit(1)

    # Connect ...
    info = infolist[0] # per standard recommendation, try the first one
    socket_args = info[0:3]
    address = info[4]
    # pass the three elements of socket_args as three separate args
    s = socket.socket(*socket_args)
    try:
        s.connect(address)
    except socket.error as e:
        print("Network failure:", e.args[1])
    else:
        print("Success: host", info[3], "is listening on port 80")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Try connecting to port 80")
    parser.add_argument("hostname", help="Hostname or IP address \
                                    that you want to contact")
    connect_to(parser.parse_args().hostname)
