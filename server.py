# Server program

import socket
from _thread import *

# **********************************************************************
# ADD the IP-address of your computer and pick a Port:
IP = '192.168.1.18'
PORT = 2345
# **********************************************************************


# List of all the sockets connected to the server.
connections = []

# Functions

def connection(sock, addr):
    connections.append(sock)

    print(f"Connection with {addr} established!")
    sock.send("Connected".encode())

    while True:
        broadcast(input("Write message:\n"))
        recive()


def broadcast(string):
    for sock in connections:
        sock.send(string.encode())


def recive():
    for sock in connections:
        msg = sock.recv(1024)
        print(msg.decode())
        if msg.decode().__eq__("Disconnecting, bye!"):
            connections.clear()
            exit_thread()


# Creating a socket for the server, listening for incoming connections.
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((IP, PORT))

serverSocket.listen()

print("Listening for connections...")

# Accepting new connections and starting new threads for each.
while True:
    clientSocket, address = serverSocket.accept()
    start_new_thread(connection, (clientSocket, address))
