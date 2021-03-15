# Client program

import socket
import sys
import random

# Array and string containing valid bot names.
valid_botnames_ary = ['alice', 'bob', 'dora', 'cs']
valid_botnames_str = ""
for name in valid_botnames_ary:
    valid_botnames_str += name + " "


# Bots
# **********************************************************************
# NOTE!:
# I created one bot myself (cs) and decided to pick some from the suggested ones,
# since I didn't really see it as part of the technical challenge we were presented with.
# **********************************************************************

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

def dora(a, b = None):
    alternatives = ["coding", "singing", "sleeping", "fighting"]
    b = random.choice(alternatives)
    res = "Yea, {} is an option. Or we could do some {}.".format(a, b)
    return res, b

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

    words_from_input = array_to_letters(msg.decode().lower().split())
    recognizable_words = {'bye', 'hi', 'hello', 'cry', 'code', 'laugh', 'eat', 'sing', 'play', 'dance',
                          'party', 'hug', 'talk', 'run'}
    words_recognized = []

    for word1 in recognizable_words:
        for word2 in words_from_input:
            if word1.__eq__(word2):
                words_recognized.append(word1)

    print(words_recognized)

    # Creating a reply
    if "bye" in words_recognized:
        connected = False
        clientSocket.send("Disconnecting, bye!".encode())
        clientSocket.close()
    else:
        reply = ""
        reply += innBot + ": "
        if len(words_recognized) > 1:
            reply += eval(innBot + "(ArrayOfMutualWords[0], ArrayOfMutualWords[1])")
        elif len(words_recognized) == 1:
            reply += (eval(innBot + "(ArrayOfMutualWords[0])"))
        else:
            reply += "I dont have any reply to that"
        clientSocket.send(reply.encode())
