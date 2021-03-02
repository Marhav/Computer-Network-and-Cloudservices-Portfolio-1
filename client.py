# Client program

import socket
import sys

'''
def alice(a, b = None):
    return "I think {} sounds great!".format(a + "ing")

def velgBot(bot):
    switcher = {
    "alice": alice(msg)
}
'''
ip = sys.argv[1]
port = sys.argv[2]
#innBot = sys.argv[3]

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((ip, int(port)))

msg = clientSocket.recv(1024)

print(msg.decode())

msg = ""

connected = True
while connected:
    # Reciving message
    msg = clientSocket.recv(1024)
    print(msg.decode())

    if (msg.decode().__eq__("Bye")):
        connected = False
        clientSocket.send("Disconnecting, bye!".encode())
        clientSocket.close()
    else:
        msg = input("Write message:\n")
        clientSocket.send(msg.encode())

