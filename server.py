# Server program

import socket
from threading import *

def connection(socket, addr):
    connected = True
    while connected:
        msg = input("Write message:\n")
        clientSocket.send(msg.encode())

        msg = clientSocket.recv(1024)
        print(msg.decode())
        if msg.decode().__eq__("Disconnecting, bye!"):
            connected = False

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('192.168.1.18', 2345))

serverSocket.listen(1)
th = []

connections = []

print("Listening for connections...")

while True:
    clientSocket, address = serverSocket.accept()

    connections.append(clientSocket)

    print(f"Connection with {address} established!")
    clientSocket.send("Connected".encode())

    th.append(Thread(target=connection, args=(clientSocket, address)).start())

