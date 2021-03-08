# Server program

import socket
from _thread import *

connections = []


def connection(sock, addr):
    connected = True
    while connected:
        broadcast(input("Write message:\n"))
        recive()


def broadcast(string):
    for sock in connections:
        sock.send(string.encode())


def recive():
    for sockk in connections:
        msg = sockk.recv(1024)
        print(msg.decode())
        if msg.decode().__eq__("Disconnecting, bye!"):
            connected = False


serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('192.168.1.18', 2345))

serverSocket.listen(5)

print("Listening for connections...")

while True:
    clientSocket, address = serverSocket.accept()
    connections.append(clientSocket)
    start_new_thread(connection, (clientSocket, address))

    print(f"Connection with {address} established!")
    clientSocket.send("Connected".encode())