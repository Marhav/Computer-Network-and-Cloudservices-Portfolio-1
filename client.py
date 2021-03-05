# Client program

import socket
import sys

# Bots

def alice(a, b=None):
    return "I think {} sounds great!".format(a + "ing")


def bob(a, b=None):
    if b is None:
        return "Not sure about {}. Don't I get a choice?".format(a + "ing")
    return "Sure, both {} and {} seems ok to me".format(a, b + "ing")


# Functions

# Takes in an array and removes everything but letters.
def array_to_letters(input):
    array = []
    for i in input:
        array.append(''.join(filter(str.isalpha, i)))
    return array


# Input arguments

ip = sys.argv[1]
port = sys.argv[2]
innBot = sys.argv[3]


#Connecting to server

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

    ArrayOfIncommingWords = array_to_letters(msg.decode().lower().split())
    ArrayOfMeaningfulWords = {'cry', 'code', 'laugh', 'eat', 'bye'}
    ArrayOfMutualWords = []

    for word1 in ArrayOfMeaningfulWords:
        for word2 in ArrayOfIncommingWords:
            if word1.__eq__(word2):
                ArrayOfMutualWords.append(word1)

    print(ArrayOfMutualWords)


    # Creating a reply
    if "bye" in ArrayOfMutualWords:
        connected = False
        clientSocket.send("Disconnecting, bye!".encode())
        clientSocket.close()
    else:
        if len(ArrayOfMutualWords) > 1:
            reply = eval(innBot + "(ArrayOfMutualWords[0], ArrayOfMutualWords[1])")
        elif len(ArrayOfMutualWords) == 1:
            reply = eval(innBot + "(ArrayOfMutualWords[0])")
        else: reply = "I dont have any reply to that"
        clientSocket.send(reply.encode())