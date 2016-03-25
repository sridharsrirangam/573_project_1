#!/usr/bin/python           # This is server.py file

import socket               # Import socket module


   


server = socket.socket()         # Create a socket object
server_host = socket.gethostname() # Get local machine name
server_port = 7734               # Reserve a port for your service.
server.bind((server_host, server_port))        # Bind to the port

server.listen(5) # Now wait for client connection.
print 'server is listening on port',server_port
while True:
   client_socket, client_addr = server.accept()     # Establish connection with client.
   print 'Got connection from', client_addr
   client_socket.send('Thank you for connecting \n')
   a = client_socket.send('this is also a message too')
   print a
   print client_socket.recv(1024)
   client_socket.close()                # Close the connection
