#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter03/tcp_sixteen.py
# Simple TCP client and server that send and receive 16 octets

import argparse, socket

def recvall(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFerror('was expecting %d bytes but only received'
                           ' %d bytes before socket closed'
                           % (length, len(data) ))
        data += more
    return data

def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print('client has been assigned socket name', sock.getsockname()) 
    sock.sendall(b'Hi, there server')
    reply = recvall(sock, 16)
    print('the server said', repr(reply))
    sock.close

def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # This tuple identifies *passive* (listening) socket
    sock.bind((interface, port))
    sock.listen(1)
    print('listening at', sock.getsockname())
    while True:
        sc, sockname = sock.accept()
        print('\nwe have accepted connection from ', sockname)

        # This four-tuple identifies *active* socket
        print('  socket name: ', sc.getsockname())
        print('  socket peer: ', sc.getpeername())

        message = recvall(sc, 16)
        print('incoming 16-octet message: ', repr(message))
        sc.sendall(b'Farewell, client')
        sc.close()
        print('  reply sent, socket closed')

if __name__ == '__main__':
    choices = { 'client': client, 'server': server }
    parser = argparse.ArgumentParser(description='send and receive over TCP')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='interface the server listens at;'
                        ' host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='UDP port (default 1060)')

    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)

