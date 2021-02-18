import socket

# create client socket opject
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# define host and port
host = '192.183.9.102'
# host = socket.gethostname()
port = 444

# connect to the server
clientsocket.connect((host, port))

# receive message from server, limit message
message = clientsocket.recv(1024)

# close connection
clientsocket.close()

# print message
print(message.decode('ascii'))
