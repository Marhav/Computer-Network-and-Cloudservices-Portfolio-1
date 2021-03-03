# Client program

import socket
import sys


def alice(a, b=None):
    return "I think {} sounds great!".format(a + "ing")


def bob(a, b=None):
    if b is None:
        return "Not sure about {}. Don't I get a choice?".format(a + "ing")
    return "Sure, both {} and {} seems ok to me".format(a, b + "ing")


ip = sys.argv[1]
port = sys.argv[2]
innBot = sys.argv[3]

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((ip, int(port)))

msg = clientSocket.recv(1024)
print(msg.decode())

msg = ""

connected = True
while connected:
    # Receiving message
    msg = clientSocket.recv(1024)
    print(msg.decode())

    if msg.decode().__eq__("bye"):
        connected = False
        clientSocket.send("Disconnecting, bye!".encode())
        clientSocket.close()
    else:
        # msg = input("Write message:\n")
        ArrayOfIncommingWords = msg.decode().split()
        ArrayOfMeaningfulWords = {'cry', 'code', 'laugh', 'eat'}

        ArrayOfMutualWords = []

        for word1 in ArrayOfMeaningfulWords:
            for word2 in ArrayOfIncommingWords:
                if word1.__eq__(word2):
                    ArrayOfMutualWords.append(word1)


        print(ArrayOfMutualWords)

        if len(ArrayOfMutualWords) > 1:
            reply = eval(innBot + "(ArrayOfMutualWords[0], ArrayOfMutualWords[1])")
        else:
            reply = eval(innBot + "(ArrayOfMutualWords[0])")
        clientSocket.send(reply.encode())

