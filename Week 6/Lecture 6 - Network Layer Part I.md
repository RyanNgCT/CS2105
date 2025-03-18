## A. Introduction to Network Layer
#### Motivation
- understand how large systems are made, how to understand a large scale application (integration and interfacing with different machines)
- engineering problem disguised as a networking course

**Previous Problem (with already proposed solutions)**
- building Internet to offer web services
- don't know where Bob is sitting $\implies$ concept of domain name
	- TCP is a means of establishing a connection from Alice to Bob
- achieving reliable data transfer over unreliable medium (achieved by `rdt`), i.e. IP
- have to ensure that a (postal) network has to be linked together
- there are certain sub-problems

#### What is the Network Layer?
- entire infrastructure that the Internet is build upon using IP
	- the binding glue, single most important protocol
- can learn anything about network layer without knowing much things about the other layers in the TCP/IP model
- the network layer delivers packets to receiving host or endpoints
- consists of three main protocols
	- routing protocols (for path selection) $\implies$ RIP, OSPF and BGP
	- internet protocol (specifies addressing conventions, datagram format and packet handling conventions)
	- Internet Control Messaging Protocol  (a.k.a. `ping`) to use for error reporting and router "signalling

- A router is a device that has $\geq 2$ interfaces  or ports and it is ready to receive and forward data
	- enables data transfer between $\geq 2$ networks

- ⚠️ *shortest could be in term of any parameter (not just time, but cost etc.)*

**Sub Problems**
- Unique Addressing for each host
- Find the path between **all pairs** of hosts and destinations (to be determined)
- protocol for service guarantee between the networks and on a common addressing scheme interpreted by member networks (i.e. the routers should enforce this)
- need to find **cooperating** path of routers to transmit the data
	- the internet is connected by multiple connected networks
	- not manipulated or will steal data being transmitted

- unlike a mail networks, every router on the Internet **must use the same protocol** (i.e. Internet protocol)
	- Last two are administrative (they are not engineering problems) $\implies$ can be done with the means of paying someone

#### Purpose
- **forward:** to send packets (by means of sorting) $\implies$ only looking at the next hop, no intelligence involved
- **route:** *deciding what is the best path to take*
	- is an end-to-end decision and so it is done **before** the forwarding option is done.
	- shortest route
	- cost of the route
	- security versus normal (no encryption)

#### Overview
- only two people need to agree for a application layer protocol to need to work
- transport layer protocols are a set of rules and symbols to cooperate
	- address is readable (network provides), but only Alice and Bob need to know how to read it (so still two)
- as a network protocol designer, we need to wear the hat of:
	- a designer
	- an implementor of the protocol

## B. IP Addressing
- used for identifying various hosts and routers
- is a $32$-bit integer (4 bits) expressed in either binary of decimal
	- can have only up to $\approx 4$ billion IPv4 addresses
- IP addresses need to be globally unique

- hosts obtain IP address with the help of
	- **manual configuration** by sysadmin via GPO or Windows configuration dialog
	- **automatic configuration** using Dynamic Host Configuration Protocol server

- IP address belongs to an **interface**, not a host!
	- each host has to have at least one interface
	- each router must have more than one interface

- IP address may be dynamic in the case when moving across physical locations
	- IP can be collected back when one leaves the network

- IP address is a binary sequence, **not an integral number**
	- compare the network portion of the IP address
#### Forwarding Table
- what the router should do when he obtains a packet with a specific IP address
- keep track of the # host that it is connected to $\implies$ inefficient
	- address aggregation enables us to significantly reduce the size of the forwarding table by grouping chunks of IP address
	- address aggregation enables IPs of the same kind to start with the same prefix

#### Reserved Addresses
Refer to RFC 5735
1. Non-routable $\implies$ `0.0.0.0/8` (which is also used for DHCP)
2. Loopback interface $\implies$ `127.0.0.1/8` (although mask is usually `/32` in CIDR)
3. Private addresses $\implies$ `10.0.0.0/8`, `172.16.0.0/12` and `192.168.0.0/16`\
4. Broadcast $\implies$ `255.255.255.255/32`

#### Network Interfaces
- host typically has one or two network interfaces (WiFi, Ethernet/LAN)
- router typically has multiple interfaces (internal and external facing)
#### Subnet
> **Subnet** is a network formed by a group of "directly" interconnected hosts.
- hosts in the same network have the same subnet (or network) prefix
- hosts in same subnet can physically reach each other **without involving router** and have the **same subnet prefix**
- connect to outside world or other subnets by means of a router

- Between routers, we have subnets as well
	- directly connected, form a subnet as well
	- the moment we use a routing interface, it is not a subnet.

- subnet mask, perform logical **AND**
#### Classless Inter-domain Routing (CIDR) notation
- subnet prefix of IP address is of arbitrary length
- address format is `a.b.c.d/x`, $x$ refers to the # bits in the subnet (or network prefix)
- then number of possible hosts is $2^{32 - x}$.
#### IP Address Allocation
- IP address "blocks" are bought from registry (for large organizations) or rented from one's ISP shared address space
	- ISP may use addition bits to differentiate between sub entities

- Hierarchical Addressing is a common practice to ensure efficient advertisement of routing information
	- leads to smaller routing tables

## C. Network Address Translation
- limited number of IP address
- have ran out of IPv4 addresses
- solves the collision posed by private IP addresses
	- public IP address sort of uses a proxy mechanism of all communications

- use of the NAT translation table to keep track of the WAN IP/port mapping to the LAN IP/port mappings
	- idea of NAT server is to have the service on the edge router of organizations etc. (acts as a proxy to the outside world)

- Using the Private IP addresses does not guarantee uniqueness (can have two hosts in different networks using the same IP to request a resource)
	- cannot be used for routing on the Internet

- all connections are uniquely identified by the four-tuple:
	- `src_ip` (will all be the same regardless of host), `dst_ip`
	- `src_port`, `dst_port`
		- degree of freedom is determined by the randomly chosen `src_port` in the address translation from private to public

	- incoming connections, `dst_ip` and `dst_port` is replaced with the corresponding client's tuple as stored within the NAT translation table

### NAT Implementation
- routers must replace the source IP and port of every outdoing datagram to the "master" NAT IP address and port
- routers need to remember the mapping from source IP and port to NAT IP and port
- routers must replace NAT IP address and port with the corresponding source IP and port stored in the NAT translation table for every incoming datagram packet.
- good alternative to IPv6 (a much more elegant solution)
	- NAT is an invisible piece of technology to resource providers

- possible to have a hierarchy of NAT servers
- we can have up to $2^{16} - 1024 \approx 64,000$ connections
- because the limiting factor is the port number field, which is 16-bits in length)
	- need to subtract common port numbers as well

## D. Dynamic Host Configuration Protocol (DHCP)
#### Motivation
- when we first turn on our computer and connect to a network, we have no information about our IP address, which is crucial for sending information and communicating with other hosts within the network $\implies$ how does a host obtain an IP address
- should function seamlessly in a plug-and-play fashion

#### Properties
- allows hosts to **dynamically obtain** IP address from DHCP server when it first joins the network (DHCP DORA)
	- IP address is "leased" to endpoints and can be renewed
	- ==allows for the re-use of addresses, only hold address while connected (??)== $\implies$ restriction is only having 100 active users at a time (limited to $2^n$, where $n$ is # host bits)
	- supports mobile users to join network (no manual config on end user's end)

- ⭐DHCP Server runs on port `67`, while the client runs on port `68`, on top of UDP.
	- DHCP is an **application layer** protocol (*is not a network layer protocol*) since it sits above UDP and in turn, IP.
	- is required for the proper functioning of the network layer

#### Steps
Discover, Offer, Request, Acknowledge (DORA)
1. **Discover** Phase: client sends packet with the following
	1. `ip_src` : `0.0.0.0`
	2. `ip_dst`: `255.255.255.255` (*broadcast* within local network)
	3. `src_port`: `68`
	4. `dst_port`: `67` (happens to be the one that the DHCP server is listening on)
	5. `yiaddr`: `0.0.0.0`
	6. `transactionId`: $n$, arbitrarily determined

2. **Offer** Phase: DHCP server responds with lease IP
	1. `src_ip`: `192.168.0.3`
	2. `dst_ip`: `255.255.255.255` (broadcast within local network again because we might not know how requested for it)
	3. `src_port`: `67`
	4. `dst_port`: `68`
	5. `yiaddr`: `192.168.0.10` (leased IP)
	6. `transactionId`: $n$
	7. `lifetime`: `3600`s (lifetime of the lease)

3. **Request** Phase: client requests for IP address
	1. `ip_src` : `0.0.0.0`
	2. `ip_dst`: `255.255.255.255`
	3. `src_port`: `68`
	4. `dst_port`: `67`
	5. `yiaddr`: `192.168.0.10` (leased IP)
	6. `transactionId`: $n + 1$
	7. `lifetime`: `3600`s

4. **Acknowledge** Phase: DHCP server approves request for the set lifetime
	1. `src_ip`: `192.168.0.3`
	2. `dst_ip`: `255.255.255.255`
	3. `src_port`: `67`
	4. `dst_port`: `68`
	5. 5. `yiaddr`: `192.168.0.10` (leased IP)
	6. `transactionId`: $n + 1$
	7. `lifetime`: `3600`s

#### ⚠️ Important Notes: 
- Lifetime field is only populated after Offer stage.
- `transactionID` field denotes which Offer is for which corresponding Discover.
- why the need to send "another" request when we already have an offer?
	- mitigate the case of multiple DHCP servers $\implies$ multiple DHCP servers responding to the offer, so only can pick 1 offer (property that IP address has to be unique applies in private network as well).

#### More on DHCP
- is a configuration protocol, so it provides much more than just merely IP address 
	- IP address of *local DNS server, default gateway* (first-hop router) and *DHCP Server*
	- Network mask to indicate the network prefix that has been configured

## E. Datagram Format & Fragmentation
- IP Header Format is quite detailed-oriented
- looking at a particular issue with reduced link capacity

- IP fragmentation enables us to carry out host-to-host communication across multiple links
- The purpose of the network layer is to provide a service abstraction to upper layers that it supports, which include the transport and application layers

#### IP Datagram Format
Made of of a 20 byte header
- IP version (4 bits)
- IP datagram length (16 bits), describes how long the header and IP data are.

- Time to Live (8 bits) $\to$ how long it is allowed to live in the core network
	- allowed to live for only $n$ hops. Router $i$ reduces the TTL field to $n-1$ each time.
	- is a failsafe mechanism

- Upper Later Protocol (8 bits) $\to$ typically TCP or UDP
- Header Checksum (16 bits)
	- this is recalculated before transmission at each hop, since the TTL field is decremented by 1 each time.

- Source IP (32 bits)
- Destination IP (32 bits)

- thereafter followed by the data

#### IP Fragmentation
- different physical links may have capacity / different maximum transfer unit (MTU)
	- it is the largest amount of data that a link level (ethernet) frame can carry

- we may have IP datagrams which are too large to be fragmented by the routers $\implies$ one datagram becomes several smaller datagrams (or smaller MTUs)

- fragmentation can be done at the router level, while reassembly is only done at the destination

- IP header has mechanisms to capture fragmentation and reassembly information, namely
	- identifier
		- `id` field will **only be the same for fragments** from the **same (bigger) datagram** which was fragmented
	- flags
		- `frag`: set to $1$ if $\exists$ a next fragment incoming, $0$ if **no subsequent segments** (the last one)
			- also not set if size $\leq$ MTU (i.e. no fragment needed).
	- fragment offset
		- captures the byte offset (but counts in units of 8-bytes, or is DWORD aligned)
			- have to divide the offset by 8 ($\div 8$)
		- only relevant when there is an offset present

- fragmentation is done on a contiguous basis (so that reassembly is easier)