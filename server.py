# Server program

import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('10.45.236.167', 9998))

serverSocket.listen(1)

while True:
    print("Listening for connections...")

    clientSocket, address = serverSocket.accept()
    print(f"Connection with {address} established!")

    clientSocket.send("connected".encode())

    connected = True
    while connected:
        msg = input("Write message:\n")
        clientSocket.send(msg.encode())

        msg = clientSocket.recv(1024)
        print(msg.decode())
        if (msg.decode().__eq__("Disconnecting, bye!")):
            connected = False
