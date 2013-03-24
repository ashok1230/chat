import socket                       # Import socket module
s = socket.socket()                 # Create a socket object
host = socket.gethostname()         # Get local machine name
port = 12345                        # Reserve a port for your service.
s.bind((host, port))                # Bind to the port
s.listen(5)                         # Now wait for client connection.
c, addr = s.accept()             # Establish connection with client.
print 'Got connection from', addr
data='thanku for connecting'
print data
try:
    while True:
	data=raw_input("server:")
	if data != 'quit':
   	    c.send(data)
	    msg=c.recv(1024)
	    if msg != 'quit':
   	    	print 'client:',msg 
	    else:
	       	print 'client:',msg
		c.send('ok, bye')
               	c.close()
	       	break 
	else:
	    c.send(data)
	    ms=c.recv(1024)
	    print ms
	    c.close()
	    break
except socket.error:
    print 'chat connection closed by client'