### Introduction

Where the coding interview serves primarily as an assessment of your problem-solving ability, the systems design interview is a test of your engineering knowledge veiled behind the facade of an open-ended design question.

### What Are Design Fundamentals?

Building scalable, production-ready applications is both art and science. Science, in that it requires knowledge of many topics in computer engineering; art, in that it demands an eye for making smart design choices and piecing together the right technologies.

Master both disciplines and you, too, can become a Systems Expert.

### Client Server Model

A client is a thing that talks to servers. A server is a thing that talks to clients. The client—server model is a thing made up of a bunch of clients and servers talking to one another.


**Key Terms**

_Client_: A machine or process that requests data or service from a server.

Note that a single machine or a piece of software can be both a client and server at the same time. For instance a single machine could act like a server for end user and as a client for the database.

_Server_: A machine or process that provides data or service for a client, usually by listening for incoming network calls.

Note that a single machine or a piece of software can be both a client and server at the same time. For instance a single machine could act like a server for end user and as a client for the database.

_Client-Server Model_: The paradigm by which the modern systems are designed, which consists of client requesting data or service from the servers and servers providing data or service to clients.

_IP Address_: An address given to each machine connected to the public internet. IPV4 addresses consists of four numbers separated by dots: **a.b.c.d** where all four numbers are between 0-255. Sepecial values include:

- 127.0.0.1: Your own local machine. Also referred to as **localhost**.
- **192.168.x.y** your private network. For instance, your machine and all the machines connected to your private wifi network, will usually have the **192.168** prefix.

_Port_: In order for multiple programs to listen for a new network connections on the same machine without colliding, they pick a **port** to listen on. A port is an integer between 0 and 65,535 (2^16 ports total).

Typically, ports 0-1023 are reserved for system ports (also called _well-known_ ports) and shouldn't be used by user level processes. Certain ports have pre-defined uses, and although you usually won't be required to have them memorized, they are sometimes comes in handy. Below are some examples:

- 22:  Secure shell
- 53:  DNS lookup
- 80:  HTTP
- 443: HTTPS

_DNS_: Short for Domain Name System, it describes the entities and protocols involved in the translation from domain names to IP Adresses. Typically, machine make a DNS query to a well known entity which is responsible for returning the IP Address (or multiple ones) of the requested domain name in the response.


Helpful Resource
1. [Netcat (nc) Command with examples](https://linuxize.com/post/netcat-nc-command-with-examples)
2. [Netcat (nc) tutorial point](https://www.tutorialspoint.com/unix_commands/nc.htm)
3. [Private IP address lookup](https://phoenixnap.com/kb/how-to-find-ip-address-linux#ftoc-heading-5)
