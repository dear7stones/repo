import socket

s = socket.socket()
host = socket.gethostname()
port = 12222

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))

s.listen(5)
c = None

while True:
	if c is None:
		print(' [Waithing for connection ...]')
		c, addr = s.accept()
		print( 'Got Connection from', addr)
	else:
		print( '[Waithing for response ...]')
		print((c.recv(1024)).decode('utf-8'))
		q = input("Enter Something to this client: ")
		c.send(q.encode('utf-8'))