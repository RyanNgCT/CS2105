## 2.1 Principles of Network Applications
- application layer protocol used by every single Internet Application
- network applications run on hosts or endpoints and contain communicating processes

### Application Architectures
#### 1. Client-Server Model
- has a server process that waits to be contacted (through incoming requests)
- also has a client process that initiates the connection with the server
	- typically requests for a particular service (i.e. file resource, file download, data etc.)
	- for web usage (using `http` and `https` protocols), the client is usually implemented with the use of a browser

#### 2. Peer-to-Peer (P2P)
- No such this as always on (has downtime in consideration)
- arbitrary endpoints directly communicate with each other
- each endpoint (a peer) requests for services, which are provided by other peers (i.e. peers are classified on the similar level)

**Advantage**
- Highly scalable

**Disadvantage**
- ==Difficult to manage (?)==

####  3. Hybrid
- uses a combination of client-server and P2P model
- i.e., using a chatting service between two users

- presence detection or location is centralized
	- each user or endpoint first registers their IP address with a central server when they are first online
	- user contacts the central server to find IP address of targets they wish to communicate with, that are within the scope of the hybrid network.

## 2.1a Network Transport and Protocols
Key Question to ask: What (kind of) transport service does an app need?
- i.e. the factors to consider when selecting a transport service

**Ensuring Data Integrity**
- some applications may require 100% reliable data transfers (i.e. no breakage in the connection)
- other applications like audio streaming might be able to tolerate some data loss

**Ensuring Throughput**
- multimedia

## 2.2 Web and HTTP


## 2.4 DNS