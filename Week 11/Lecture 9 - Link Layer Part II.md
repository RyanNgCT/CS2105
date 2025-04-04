- building a network that only spans our office or dorm
- how to connect $N$ nodes via a single cable
- why do we need to have a protocol
	- error detection and recovery (not the primary concern)
	- need to access the shared medium (access control)

- need to know who the packet is for
	- introduces error detection, frame construction and link access control

- a hub allows us to connect all the nodes in the network (a more stupid switch)
	- hub can be use to connect $\geq 1$ hubs (rather than connecting to the nodes themselves)
- network can be restricted by the length of cables (maximum length of the diameter of the network)
## Introduction to LAN
- LAN is a network that spans within a geographical area (usually a building or university campus)
- can have multiple subnets inside of it
- is not defined by the technology (can be implemented using $\geq 1$ technologies)
### Ethernet
- is the dominant wired LAN technology
- is cheaper and simpler than the IBM token ring and the ATM model
#### Ethernet 802.3 Standards
- is a family of standards developed over the years
- have the same MAC protocol and frame format
- different speeds and physical layer media
- everything is implemented on the NIC card
- Suffix of `X` $\implies$ fibre
- `T` $\implies$ twisted pair physical layer cables
#### Ethernet Frame Structure
- consider the case of sending IP datagram to the next hop on the same ethernet
- the sending NIC adapter encapsulates IP datagram in the Ethernet frame
- can only send the data to a node **within the same subnet** (cannot send outside the subnet)
	- is the job of network layer to make sure it reaches the recipient

**Components:**
- Preamble
- `src_addr` : 6 byte MAC address
- `dst_addr` : 6 byte MAC address
- `type`
- Data $\implies$ 1500 bytes
- CRC

**Type**
- Ethernet and IP are not the only protocol with a dependence relation
	- need to keep in mind that hosts can use other network-layer protocols besides IP (i.e. ARP)
- permits ethernet Ethernet to multiplex network layer protocols

**Preamble**
- indication that we are sending an ethernet frame
- having a clock and having all devices synchronized is an expensive task
	- the patterns of $7 \times 10101010_2$ to indicate that we should synchronize the clocks
	- clock should be good enough to maintain its synchronization for $\geq 1500$ bytes

**Length, min and max length**
The size of the frame is bounded by the upper and lower limits of $[46, 1500]$
- MTU $= 1500$ bytes

What is the size or the length of the data?
- there is something called the Inter-frame gap which is introduce to demarcate the end of a frame
#### Ethernet Data Delivery Service
- is inherently unreliable: receiving NIC doesn't send ACK or NACK
	- data in drop frames will be recovered only if initial sender uses higher layer rdt (i.e. TCP), otherwise dropped data is lost (up to higher layer to implement reliability)

- ethernet multiple access protocol: using CSMA/CD will binary backoff

#### Ethernet Bus Topology
- is a broadcast LAN (all transmitted frame received by all adapters connected to the bus)
	- all nodes can collide with each other

- single point of failure (backbone cable)
- difficult to troubleshoot problems
- very slow and not ideal for large network $\implies$ collisions
#### Ethernet Star Topology
- more prevalent today, with a hub (works at the physical layer)
##### Hub
- a hub is a physical layer device that acts on a individual bit level
- costs of having a star topology (look at the disadvantages)

**Advantages**
- cheap
- easy maintenance (modular in nature)

**Disadvantages**
- limited by # ports (not exactly a drawback)
- still a single point of failures
- number of cables
- still have lots of collisions (realm of broadcast medium)
##### Switch
- is a layer 2 device
	- works on frames rather than individual bits
	- store-and-forward
		- it has buffers and waits for the entire frame to arrive before forwarding

- does not amplify signals, but rather works on frames
- has no collisions
### Ethernet Switch
- link layer devices used in LANs
	- examine the incoming frame's MAC address and selectively forward the frame to one-or-more outgoing links
- stores and forwards ethernet frames
- uses CSMA/CD to access link

- is a Transparent
	- hosts are unaware of the presence of the switch (appears to be going directly to the next hop)

- is plug-and-play (self-learning) $\implies$ switch don't require configuration

- remove collisions, thus network is much faster
#### Multiple Simultaneous Transmissions
- nodes have a dedicated, direct connection to the switch $\implies$ have **no collisions**, but CSMA/CD is maintained for backward compatibility

- every interface has an incoming and outgoing buffer
	- transmitting the frame is merely just doing a memory copy operation from the incoming buffer to the outgoing buffer
	- can simultaneously transfer packets multiple different hosts, but cannot simultaneously transfer to the same host

- format of entry in switch table:
	- `mac_addr`,`interface_id`, `ttl`
	- `ttl` fields ensures the entry does not go stable

- self-learning property of the switch
	- we have a mapping on the `src_MAC` address to the interface
	- if $\not \exists$ entry for a particular mapping, then we store the packet in the buffer first
		- send to all the other interfaces except for the one that it was sent from

- switch has only can recreate data packets, and it does not have a MAC address

- switching table entries are updated upon broadcast

**Scenario**
1. receive packet, where `dst_addr` unknown
2. receive packet, where `dst_addr` known
3. filter or drop packet

- MAC address $\implies$ only need unique one hop (i.e. Virtual Machine to host comms)