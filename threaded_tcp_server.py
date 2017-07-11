#!/usr/bin/python
# Simple multi-threaded TCP server
import socket
import threading

ip   = "0.0.0.0"
port = 9999

# create socket
server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

# bind socket
server.bind( ( ip, port ) )

# listen for connections
server.listen(5)
print "[*] Listening on %s:%d" % ( ip, port )

# thread to handle connections
def handle_client(client_socket):

    # print what client sends
    request = client_socket.recv(1024)
    print "[*] Received: %s" % request

    # send back a packet
    client_socket.send("ACK!")
    print client_socket.getpeername()
    client_socket.close()

# accept connections
while True:
    client, addr = server.accept()

    print "[*] Accepted connection from: %s:%d" % ( addr[0], addr[1] )

    # handle incoming data
    client_handler = threading.Thread( target = handle_client, args = (client,) )
    client_handler.start()
