- these days even performance-critical apps (like message queues) use TCP
- UDP shines when a long term relationship between client/server is not needed

TCP basics
----------

All the app sees is a stream of data; the actual packets and sequence numbers are hidden away by the OS net stack.

TCP provides reliability via:
- sequence numbers (retransmission, reordering): the initial is chosen randomly, icremented by the number of transmitted bytes
- windows (flow control, splitting data) - the amount of data the sender is willing to have on the wire at any given moment

TCP connection setup:
1. SYN: "I wanna talk, here's my initial sequence number"
2. SYN-ACK: "OK, here's my initial sequence number"
3. ACK: "Okay!"
```
09:27:43.581467 IP 127.0.0.1.35344 > 127.0.0.1.1060: Flags [S], seq 3343397715, win 43690, options [mss 65495,sackOK,TS val 2441162 ecr 0,nop,wscale 7], length 0
09:27:43.581486 IP 127.0.0.1.1060 > 127.0.0.1.35344: Flags [S.], seq 2281572072, ack 3343397716, win 43690, options [mss 65495,sackOK,TS val 2441162 ecr 2441162,nop,wscale 7], length 0
09:27:43.581498 IP 127.0.0.1.35344 > 127.0.0.1.1060: Flags [.], ack 1, win 342, options [nop,nop,TS val 2441162 ecr 2441162], length 0
```

TCP connection shutdown:
1. FIN
2. FIN-ACK (or separate ACK and FIN)
3. ACK

Sockets
-------

- it takes only a single socket to speak UDP
- you need both passive (listening) and active (connected) socket for TCP

listening socket
- no data
- to alert the OS of the willingness to receive connections on a TCP port

connected socket
- bound to one particular remote conversation partner with particular IP address and port
- stream looks like a pipe or file
- can be many

TCP server, client
------------------

See `tcp_srv_cli.py`.

Typical TCP stacks use **buffers** - both so that they have somewhere to place incoming packet data until an application is ready to read it and so that they can collect outgoing data until the network hardware is ready to transmit an outgoing packet.

When you perform `send()`, your OS's net stack will face one of:
(a) data can be immediately accepted by the net stack
(b) data buffer for *this* socket is full -> `send()` will simply block
(c) outgoing buffers are almost full -> only *part* of data can be immediately queued

Because of the (c) you have to check the return value of `send()` or use `sendall()` (there's no `recvall()`).

Half-open connections
---------------------

- socket returns empty string when it gets closed (analogical to `read(file)`
  when there's no more data in the file)

`shutdown()` can have these arguments:

- `SHUT_WR` - caller will be writing no more data, callie gets end-of-file
- `SHUT_RD` - turn off incoming socket stream
- `SHUT_RDWR` - similar to `close()` but will disable the socket for all
  processes using it

