# Client program

import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('10.45.236.167', 9998))

msg = clientSocket.recv(1024)

print(msg.decode())

msgSend = ""

connected = True
while connected:
    msgSend = input("Write message:\n")

    clientSocket.send(msgSend.encode())
    msg = clientSocket.recv(1024)
    print(msg.decode())
    if(msg.decode().__eq__("Disconnecting, bye!")):
        connected = False
