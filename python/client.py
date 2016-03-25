#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

def server_connect(server_port):
    s = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = server_port             # Reserve a port for your service.
    s.connect((host, port))
    print s.recv(1024)
    s.send('this is a message from the client')
    s.close()                     # Close the socket when done
    return

def main():
    print 'enter port of the server'
    server_port = input()
    server_connect(server_port)


if __name__ == '__main__': main()
