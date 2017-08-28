Start the server
```
./safe_tls.py -s localhost.pem '' 1234
```

Start the client
```
./safe_tls.py localhost 1234 -a ca.crt
```

If you leave out `-a ca.crt` the client will refuse to trust the server because no public authority has signed the certificate inside of localhost.pem. You will also see that the server has died, with a message indicating that the client started a connection attempt but then abandoned it.

* localhost.pem = certificate + secret key (something like: `cat localhost.crt localhost.key > localhost.pem`)
