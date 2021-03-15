# Datanettverk Portfolio 1

This assignment contains one Server program and one client program. 


## Purpose

* The server program is designed to allow multiple clients connect at once with a TCP socket and will continuously accept new incomming 
requests from clients. Furthermore the serverprogram will allow you to start a conversation with all the conected clients. The clients will 
respond differently depending on which bot the client has decided to connect with. </br></br>
The conversation work in a way that the server will ask the user for an input, when the input is given the server will broadcast the message
to all clients and then collect the replies.

* The client program is supposed to represent a bot connecting to the server. The client program require 3 input arguments to start properly, these 
are IP-address, Port and Bot-name. If the user struggles with starting the program properly there should be sufficient help to get from the 
programs error handling or the '--help'(or '-h') command. </br></br>
Once started up it will automaticly connect and expect to get a confirmation form the server saying "connected". The client will then stand by 
while awaiting new messages from the server. When a message from the server is recived the program will search the message for words that the 
bots will recognize or deem meaningful. The program will collect an infinite amount of words, but the bots will only take interest in the first two words of meaning. 

## Instructions

* Change the IP-address in the server program to match the one on your computer and pick a port of your choice. Then run the server.
* If you have trouble finding your IP, try 'ipconfig' in powershell/CMD or ifconfig in bash. 

* The client program should be run with a CMD, Bash or Powershell, as these will allow you add the input arguments needed to run the program.
* Use the same IP-address and Port that you assigned on the server as input argument 1 and 2.
* It is required that the user run the program with an existing bot. Use the '--help' command if you wonder which bots you can use.

* Once you connect a client the server will be waiting for a reply, but it will not stop accepting new clients, feel free to either connect more 
clients or start chattig right away.
