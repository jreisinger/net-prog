- these days even performance-critical apps (like message queues) use TCP
- UDP shines when a long term relationship between client/server is not needed
- all the app sees is a stream of data; the actual packets and sequence numbers are hidden away by the OS net stack

TCP basics
----------

TCP provides reliability via:
- sequence numbers (retransmission, reordering): the initial is chosen randomly, icremented by the number of transmitted bytes
- window (flow control) - the amount of data the sender is willing to have on the wire at any given moment

TCP connection setup:
(1) SYN: "I wanna talk, here's my initial sequence number"
(2) SYN-ACK: "OK, here's my initial sequence number"
(3) ACK: "Okay!"

TCP connection shutdown:
(1) FIN
(2) FIN-ACK
(3) ACK

Sockets
-------

- it takes only a single socket to speak UDP
- you need passive (listening) and active (connected) for TCP

listening socket
- no data
- to alert the OS of the willingness to receive connections on a TCP port

connected socket
- bount to one particular remote conversation partner with particular IP address and port
- stream looks like a pipe or file
- can be many

TCP server, client
------------------

See `tcp_srv_cli.py`.

When you perform `send()`, your OS's net stack will face one of:
(a) data can be immediately accepted by the net stack
(b) data buffer for *this* socket is full -> `send()` will simply block
(c) outgoing buffers are almost full -> only *part* of data can be immediately queued

Because of the (c) you have to check the return value of `send()` or use `sendall()` (there's no `recvall()`).

Typical TCP stacks use **buffers** - both so that they have somewhere to place incoming packet data until an application is ready to read it and so that they can collect outgoing data until the network hardware is ready to transmit an outgoing packet.
