import socket

# create a server socket by call socket function, define socket family and socket type
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# define host and port
host = socket.gethostbyname()
port = 444

# bind host and port to server socket
serversocket.bind((host, port))

# set up TCP listener, listen for max connections is 3
serversocket.listen(3)

while True:
    # when the client connect to server
    clientsocket, adress = serversocket.accept()

    print('Received connection from: ' + str(adress))

    # Send data back to the client
    clientsocket.send('Connection to the server success!')

    # close client connection
    clientsocket.close()
