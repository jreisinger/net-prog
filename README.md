Network Programming
===================

Sockets

- a method for IPC
- endpoints for communication
- allow processes to communicate on a host or over a network

Socket types

1) `SOCK_STREAM` - bidirectional, connection-oriented, byte-stream and reliable communication (similar
   to pipes)
   
- connection-oriented = like a phone call
- byte-stream = no concept of message boundaries
- reliable = data will be either delivered exactly as transmitted or we'll get notification of a failure

2) `SOCK_DGRAM` - only garantee that message borders will be preserverd when read
   (but lower overhead)

Domains (Protocol Families) - communication range and address format

1. `PF_INET` - socket is identified by host (IP address) and port
2. `PF_UNIX` - .. by filename (ex. `/tmp/mysock`)

... domains and types are identified by symbolic names above (that are mapped
to numeric constants) which are constants exported by `Socket` and `IO::Socket`

Protocols (there's rarely more than one protocol for the given domain and type
of socket)

1. `tcp`
2. `udp`

... protocols have names that correspond to numbers used by the OS.
`getprotobyname()` (built into Perl) returns these numbers:

    $ perl -le 'print "$_ -> ", scalar getprotobyname $_ for qw(tcp udp)'
    tcp -> 6
    udp -> 17

Perl's built-in functions

- low-level direct access to every part of the system
- on error return `undef` and set `$!`
- `socket()` - make a socket
- `bind()` - give a socket a local name by binding it to an address
- `connect()` - connect a local socket to a (possibly remote) one
- `listen()` - ready a socket for connections from other sockets
- `accept()` - receive the connections one by one creating new sockets
- use `print` and `<>` or `syswrite` or `sysread` to communicate over a stream
  socket
- .. `send` and `recv` for datagram socket
- typical SERVER: socket(), bind() and listen(); then loop in a blocking
  accept() waiting for incoming connections
- typical CLIENT: socket() and connect() // datagram clients don't need to
  connect(); they specify the destination as argument to send()

Sources

- The Linux Programming Interface, Ch. 56-61 (2010)
- Perl Cookbook, Ch. 17 Sockets (2003)
- Network Programming with Perl (2001)
- Black Hat Python (2014)
