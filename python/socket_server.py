import socket

# create a server socket object by call socket function, define socket family and socket type
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# define host and port
host = '192.183.9.102'
# host = socket.gethostbyname()
port = 444

# bind host and port to server socket
serversocket.bind((host, port))

# set up TCP listener, listen for max connections is 3
serversocket.listen(3)

# keep server always listen
while True:
    print('Server is listening!')
    # when the client connect to server
    clientsocket, adress = serversocket.accept()

    print('Received connection from: ' + str(adress))

    # Send data back to the client
    message = 'Connection to the server success!'
    clientsocket.send(message.encode('ascii'))

    # close client connection
    clientsocket.close()
