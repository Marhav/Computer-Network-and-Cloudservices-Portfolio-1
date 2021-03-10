# Client program

import socket
import sys
import random

# Array and string containing valid bot names.
valid_botnames_ary = ['alice', 'bob', 'cs']
valid_botnames_str = ""
for name in valid_botnames_ary:
    valid_botnames_str += name + " "


# Bots

def alice(a, b=None):
    if a == "hi":
        return "Hello!"
    return "I think {} sounds great!".format(a + "ing")


def bob(a, b=None):
    if a == "hi":
        return "Hello!"
    if b is None:
        return "Not sure about {}. Don't I get a choice?".format(a + "ing")
    return "Sure, both {} and {} seems ok to me".format(a + "ing", b + "ing")


def cs(a, b=None):
    if b is None:
        uselessness = random.choice(["Sorry, I can't help you with {}.".format(a + "ing"),
                                     "I don't understand, is there a problem?",
                                     "I will contact my supervisor at once!"])
        return uselessness
    uselessness = random.choice(["Do you need help with {} or {}?".format(a + "ing", b + "ing")])
    return uselessness


# Functions

# Takes in an array and removes everything but letters.
def array_to_letters(in_ary):
    array = []
    for i in in_ary:
        array.append(''.join(filter(str.isalpha, i)))
    return array


#  Checks if a bot exists.
def validate_bot(in_botname):
    valid = False

    for botname in valid_botnames_ary:
        if botname.__eq__(in_botname):
            valid = True

    if not valid:
        print("Invalid botname, valid botnames are: " + valid_botnames_str)
        exit()


# Print help instructions.
def argument_help():
    print("To run program type:\n "
          "$: py client.py <ip-address> <port> <Bot-name>\n"
          "Valid bot names are: " + valid_botnames_str)


# Input arguments

try:
    argument_1 = sys.argv[1]
except ValueError:
    print("Input argument error! Try --help")
    exit()

if argument_1.lower().__eq__('-h') or argument_1.lower().__eq__('--help'):
    argument_help()
    exit()
else:
    ip = argument_1
    try:
        port = sys.argv[2]
    except ValueError:
        print("Input argument error! Try --help")
        exit()

    try:
        innBot = sys.argv[3].lower()
    except ValueError:
        print("Input argument error! Try --help")
        exit()

    validate_bot(innBot)

# Connecting to server

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
    ArrayOfMeaningfulWords = {'cry', 'code', 'laugh', 'eat', 'bye', 'hi', 'sing', 'play'}
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
        reply = ""
        reply += innBot + ": "
        if len(ArrayOfMutualWords) > 1:
            reply += eval(innBot + "(ArrayOfMutualWords[0], ArrayOfMutualWords[1])")
        elif len(ArrayOfMutualWords) == 1:
            reply += (eval(innBot + "(ArrayOfMutualWords[0])"))
        else:
            reply += "I dont have any reply to that"
        clientSocket.send(reply.encode())
