Network Programming
===================

Sockets

- endpoints for communication
- allow processes to communicate on a host or over a network

Socket types (`man 2 socket`)

1. `SOCK_STREAM` - bidirectional, sequenced and reliable communication (similar
   to pipes)
2. `SOCK_DGRAM` - only garantee that message borders will be preserverd when read
   (but lower overhead)

Domains (Protocol Families)

1. `PF_INET` - socket is identified by host (IP address) and port
2. `PF_UNIX` - .. by filename (ex. `/tmp/mysock`)

... domains and types are identified by symbolic names above (that are mapped
to numeric constants) which are functions exported by `Socket` and `IO::Socket`

Protocols (there's rarely more than one protocol for the given domain and type
of socket)

1. `tcp`
2. `udp`

... protocols have names that correspond to numbers used by the OS.
`getprotobyname()` (built into Perl) returns these numbers:

    $ perl -le 'print scalar getprotobyname $_ for qw(tcp udp)'
    6
    17

Perl's built-in functions

- low-level direct access to every part of the system
- on error return `undef` and set `$!`
- `socket()` - make a socket
- `bind()` - give a socket a local name
- `connect()` - connect a local socket to a (possibly remote) one
- `listen()` - ready a socket for connections from other sockets
- `accept()` - receive the connections one by one
- use `print` and `<>` or `syswrite` or `sysread` to communicate over a stream
  socket
- .. `send` and `recv` for datagram socket
- typical SERVER: socket(), bind() and listen(); then loop in a blocking
  accept() waiting for incoming connections
- typical CLIENT: socket() and connect() // datagram clients don't need to
  connect(); they specify the destination an argument to send()

Sources

- Perl Cookbook, Ch. 17 Sockets
- Network Programming with Perl
