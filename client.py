import socket               # Import socket module
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.connect((host, port))
try:
    while True:
        data=s.recv(1024)
        if data !='quit': 
   	    print 'server:',data
   	    msg=raw_input("client:")
	    if msg != 'quit':
 	        s.send(msg)
	    else:
	    	s.send(msg)
		ms=s.recv(1024)
		print 'server:',ms
	    	s.close()
        else:
	    print 'server:',data
	    s.send('client:ok, bye')
	    s.close()
except socket.error:
    print 'chat connecction closed by client'    