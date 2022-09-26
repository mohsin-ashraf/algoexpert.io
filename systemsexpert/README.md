# Systems Expert


## Introduction

Where the coding interview serves primarily as an assessment of your problem-solving ability, the systems design interview is a test of your engineering knowledge veiled behind the facade of an open-ended design question.


## What Are Design Fundamentals?

Building scalable, production-ready applications is both art and science. Science, in that it requires knowledge of many topics in computer engineering; art, in that it demands an eye for making smart design choices and piecing together the right technologies.

Master both disciplines and you, too, can become a Systems Expert.


## Client-Server Model

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



## Network Protocols

**Key Terms**

_Protocol_: A set of agreed upon rules for two parties to interact with each other.

_IP_: Stands for **Internet Protocol**. This network protocol outlines how almost all machine-to-machine communications should happen in the world. Other protocols like **TCP**, **UDP**, and **HTTP** are built on top of IP.

_TCP_: Network protocol built on top of the Internet Protocol (IP). Allows for ordered, reliable data delivery between machines over the public internet by createing **connection**.

TCP is usually implemened in the kernel, which exposes **sockets** to applications that they cna use to stream data through an open connection.

_HTTP_: The **Hyper Text Transfer Protocol** is a very common network protocol implemented on top of TCP. Clients make HTTP requests, and servers respond with the response.
Requests typically have the following schema:
```
host: string (example: algoexpert.io)
port: integer (example: 80 or 433)
method: string (example: GET, POST, PUT, DELETE, OPTIONS or PATCH)
headers: pair list (example: "Content-Type" => "application/json")
body: opaque sequence of bytes
```
Responses typically have the following schema:
```
status code: integer (example: 300, 401)
headers: pair list (example: "Content-Length" => 12345)
body: opaque sequence of bytes
```

_IP Packet_: Sometimes more broadly referred to as just a (network) **packet**, an IP packet is effectively the smallest unit used to describe data being sent over **IP**, aside from the bytes. An IP packed consists of:

- an **IP header**, which contains the source and destination **IP addresses** as well as other information related to the network.
- a **payload**, which is just the data being sent over the network.

**Example**

This lesson comes with a very simple [example](./004-network-protocols) in which the request headers are being printed when someone makes a request to the server.

Helpful Resource
1. [IP Address](https://www.kaspersky.com/resource-center/definitions/what-is-an-ip-address)
2. [How TCP Works](https://www.ionos.com/digitalguide/server/know-how/introduction-to-tcp/)
3. [What is TCP](https://www.fortinet.com/resources/cyberglossary/tcp-ip#:~:text=TCP%20organizes%20data%20so%20that,remains%20live%20until%20communication%20begins.)
4. [What is HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP)
5. [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)


## Storage

**Key Terms**

_Databases_:Databases are programs that either us disk or memory to do 2 core things: **record** data and **query** data. In general, they are themselves servers that are long lived and interact the rest of your service through network calls, with protocols on top of TCP or even HTTP.

Some databases only keep records in memory, and the users of such database are aware of the fact that those records may be lost forever if the machine goes down or the process dies.

For the most part, the databases need the persistence of those records, and thus cannot use memory. This means that you have to write your data to disk. Anything written on the disk will remain through power loss or network partitions, so that's what is used to keep permanent records.

Since the machines die often in a large scale system, special disk partitions or volumes are used by the database processes, and those volumes can get recovered even if the machines were to go down permanently.

_Disk_: Usually refers to either **HDD (hard disk drive)** or **SSD (solid state drive)**. Data written to the disk will persist through power failures and general machine crashes. Disk is also referred to as **non-volatile storage**

SSD is far faster than HDD but also far more expensive from a financial point of view. Because of that, HDD will typically be used for the data that is rarely accessed or updated, but that's stored for a long time, and SSD will be used for the data which will be frequently accessed or updated.

_Memory_: Short for **Random Access Memory (RAM)**. Data stored in the memory will be lost when the process which wrote the data dies.

_Persistent Storage_: Usually refers to disk, but in general it is any for of storage that presists if the process in charge of managing it dies.


**Example**

This lesson comes with an [example](./005-storage/) explaining data stored in the memory and on the disk. The example is implemented using the nodejs for explaining how the memory data is not presistent when the server dies and the disk data is, even if you turn your machine off and then turn it back on.

Install the dependencies of the application using `npm install` and run the application using `node server.js`.

**Memory Endpoints**
```
curl localhost:3000/memory/foo --header 'Content-Type: application/json' --data '{"data": "This is some data in memory"}'
curl localhost:3000/memory/foo -w "\n"
curl localhost:3000/memory/bar -w "\n"
```


**Disk Endpoints**
```
curl localhost:3000/disk/foo --header 'Content-Type: application/json' --data '{"data": "This is some data in disk"}'
curl localhost:3000/disk/foo -w "\n"
curl localhost:3000/disk/bar -w "\n"
```


## Latency and Throughput

**Key Terms**

_Latency_: The time it takes for a certain operation to complete in a system. Most often this measure is a time duration, like milliseconds or seconds. You should know these orders of magnitude:

- Reading 1MB from RAM 250 microseconds
- Reading 1MB from SSD 1000 microseconds
- Reading 1MB from over Network 10,000 microseconds
- Reading 1MB from HDD 20,000 microseconds
- inter-Continental Round Trip:  150,000 microseconds

_Throughput_: The number of operations that a system can handle properly per time unit. For instance the throughput of a server can often be measured in requests per seconds (RPS or QPS).


Helpful Resouces
1. [Latency and Throughput](https://networkshardware.com/throughput-vs-latency/)


## Availability

**Key Terms**

_Availability_: The odds of a particular server or service being up and running at any point in time, usually measured in percentages. A server that has 99% availability will be operational 99% of the time (this would be described as having two **nines** of availability).

_High Availability_: Used to describe systems that have particularly high levels of availability, typically 5 nines or more; sometimes abbreviated "HA".

_Nines_: Typically refers to percentages of uptime. For example, 5 nines of availability means an uptime of 99.999% of the time. Below are the downtimes expected per year depending on those 9s:

```
- 99% (two 9s): 87.7 hours
- 99.9% (three 9s): 8.8 hours
- 99.99%: 52.6 minutes
- 99.999%: 5.3 minutes
```

_Redundancy_: The process of replicating parts of a system in an effort to make it more reliable.

_SLA_: Short for "service-level agreement", an SLA is a collection of guarantees given to a customer by a service provider. SLAs typically make guarantees on a system's availability, amongst other things. SLA are made up of one or multiple SLOs.

_SLO_: Short for "service-level objective", an SLO is a guarantee given to a customer by a service provider. SLOs typically  make guarantees on systems's availablity, amongst other things. SLOs constitute an SLA.

Helpful Resouces
1. [Redundancy](https://www.digitalocean.com/community/tutorials/what-is-high-availability)
2. [Nines of availability](https://en.wikipedia.org/wiki/High_availability)
