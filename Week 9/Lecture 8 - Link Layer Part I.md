## A. Introduction to the Link Layer + Motivation
- Ultimate goal of networking is to send data between $\geq 2$ nodes via a cable
	- we can do so by connecting the $2$ nodes that wish to send (and receive) data $\implies$ drawing a cable from Alice to Bob

- Can expand the above problem to $n$ nodes, i.e. send data between $n$ nodes, so we will require interconnection of $n$ nodes
	- each link needs to be addressed (the interfaces) $\implies$ to distinguish the interfaces
		- receiver has no way to know that the packet or frame belongs to him
	- need to define **protocol** for communications (i.e. set of rules to decide when and who can speak)
	- need to handle errors (they are inherent because of segment collisions)
	
- *Main drawback*: This solution **does not scale** since we require $n-1$ links

- Bus topology is a network link $\implies$ packets will be heard throughout the network
	- is scalable and cheaper
	- common cable to which everyone is connected to

**The Link Layer**
- provides communication services between any two hosts

- IP datagram may travel through multiple routers (hops) and links before reaching its ultimate destination

- The Link Layer works by sending datagrams between adjacent nodes over a single link

- we are not concerned with the larger network, but rather the communication to adjacent nodes.

- Link layer technology changes at different hops
	- only **concerned with $1$ hop** (not sending data beyond a single hop)
	- $2$ hops $\implies$ network layer

### Possible Link Layer Services
**Framing**
- allows us to encapsulate datagram into a frame and include both the header and trailer

**Link Access Control**
- when nodes share a link, need to coordinates which nodes send frames, when?

**Error Detection**
- detecting error, does not mean that it requires retransmission
- recipient detects the presence of errors (may call for retransmission or simply drops the frame)

**Error Correction**
- receiver identifies and corrects bit errors w/o resorting to retransmission

**Reliable Delivery**
- seldomly used
- not really covered

### Where is Link/Physical layer Implemented
- on the network interface itself, even lower compared to the OS (which implements transport and network)
	- implemented on the NIC itself (which can be ethernet card or WiFi adapter etc.)

### Types of Network Links
1. Point-to-Point Link
	- sender and receiver are connected by dedicated link (i.e. PPP, SLIP etc.)
	- has no need for multiple access control

2. Broadcast Link
	- multiple nodes are connected to a shared broadcast channel
	- when frame transmits frame, channel broadcasts frame and every other node receives a copy
	- has collisions, when a node receives $\geq 2$ signals at once

---
## B. Multi-Access Links and Protocols
- Multiple Access: who can talk, when they can talk and for how long
#### Motivation
- Random access protocol: No coordination, Collisions are possible
- Taking Turns: Each person gets some time to speak
- Channel Partition: divide the channel into fixed smaller pieces
- Increasing complexity as we go down (i.e. we have more rules required)

- As engineers, we will have less complexity towards the bottom, as there is more order
	- collisions are harder to recover from while coordinating and implementing scheduled messages are easier

#### Ideal Multiple-Access Protocol
- Mandatory Requirement: no out-of-band signalling
	- control signal and data **goes through the same channel**
	- recover from all failures and errors on the **same channel**
### B1. Random Access Protocols
- when node has something to send, just send (no need coordinate)
- random access protocols specify how to detect collisions and how to recover from collisions
- protocols should identify how much of the $L$ bits are the relevant data (cannot be exceeded or reduced)
#### 1. Slotted ALOHA
- has a clock
- break into packets of size $L$ bits and only transmit at a certain time slot
- No Collision $\implies$ transmission successful, Collision $\implies$ retransmit
	- retransmission using "coin toss" with probability $p$

- efficiency $\implies$ utilization (i.e. the entire bandwidth of $R$)
- is decentralised as we don't need any server. Only thing we need to synchronize or coordinate is the clock cycles
#### 2. Pure / Unslotted ALOHA
- no time slots with no synchronization
- interfered by all nodes transmitting between $t_0 - 1$ and $t_0 + 1$
- reduced efficiency as compared to Slotted ALOHA

**How do you detect a collision?**
- when we hear someone else
- when there is $\gt 1$ signal
- wait for someone to stop transmitting before (re-)transmitting

#### 3. Carrier Sense Multiple Access
- listen before transmitting
- still have the issue of collision because of propagation delay
- continues to transmit even though it detects the collision

#### 4. Carrier Sense Multiple Access / Collision Detection (CSMA/CD)
- detected by the network interface card
- don't transmit the remaining frame (time delay is for the jamming signal)
	- jamming signal to alert other nodes of collision

- the retransmission probability should keep decreasing
	- However, probability of collision stays the same
	- we can reduce the probability further on each round of collision
		- exponential backoff
		- is not deterministic since we are still using probability
	- $\uparrow$ collision $\uparrow$ backoff

- stop retransmitting after $16$ times
- If $p = 0 \implies$ retransmit immediately
##### Minimum Frame Size
- Both $B$ and $D$ cannot detect collisions when they are already done with transmitting
- Size is longer than the propagation delay?

$max(D_{\text{prop}})$ guarantees that we can communicate to the farthest node
- need to ensure that the maximum
- Transmission delay proportional to frame size
- Propagation delay proportional to the diameter of the network

- Minimum Frame Size is $64$ Bytes (determined by Ethernet Protocol)
### B2. Taking Turns Protocols
- how can we continue to have communication done effectively, even though the link medium is shared
- in between random access and channel partitioning protocols in terms of the complexity of the said protocol
#### 1. Polling
- polling protocol requires one of the nodes to be designated as the master and the remaining to be the slave nodes
- master node **polls** each of the slave nodes in a round-robin fashion
	- Underlying Principle: don't speak unless spoken to

- a poll is a special kind of frame that is sent to one endpoint device at a time.
	- slave would get the opportunity to send some amount of frames (permission to speak)

- there are certain use cases for this, even though it may seem nonsensical
	- Bluetooth Protocol (phone or PC is the master, the other devices are the slaves)
##### Steps
1. Master informs node $1$ that it can transmit a maximum of $n$ # of frames
	1. each node will broadcast the data to be sent across the entire link
2. After node $1$ transmits its frames, the master tells the subsequent node (i.e. node $2$) that it can transmit up to $n$ frames
	1. this involved node $1$ relinquishing the link
3. Cycle continues
##### Properties
1. It is **Collision Free**: there will never be a collision as 
	1. the master will poll those who will speak
	2. the master will only poll node $i$ if all the other nodes have relinquished the ability to transmit

2. We have a **higher efficiency**, but we still have the overhead associated with polling
	1. We cannot fully obtain the bandwidth

3. It is **perfectly fair**, since we are going in a round-robin fashion

4. This algorithm is **not decentralized**, because it makes use of a master node for coordination
	1. the master node is a single point of failure

#### 2. Token-passing
- a special frame, a token is passed from one node to another sequentially
- the token has to be held by a node before the node is permitted to transmit data (like a mic)
	- the node can broadcast the data to be transmitted

- if the node does not want to transmit, then it **passes the token on** to the subsequent node
	- the order of passing and time taken for the transmission by acquiring the token is predetermined
	- maximum number of frames that can be sent "per turn" is also predetermined, before relinquishing the 
	- holds onto the token only if it has frames (data to transmit)
##### Properties
1.  It is **Collision Free**: there will never be a collision as the node needs to obtain the token before transmitting

2. We have a **higher efficiency**, but we still have the overhead associated with token passing
	1. We cannot fully obtain the bandwidth (we never truly obtain the full bandwidth $R$)

3. It is **perfectly fair**, assuming no one has mess around with the implementation of the pass the token algorithm
	1. in essence, every node should get an equal amount of time for whatever transmission to be performed

4. This algorithm is **fully decentralized** once the network is fully up and running
	1. token has to willingly relinquish the token (there is no master node for enforcement)

##### Disadvantages
- the **loss of a token can be very disruptive** as we can have lost frames
	- frame getting corrupted is not rare in a network context
	- it is costly to recover from the failure (lots of effort spent, complexity of recovering from a corruption or failure)
	- introduces many system bugs

- Nodal failures are a single point of failure and can break the whole ring
### B3. Channel Partitioning Protocols
#### Time Division Multiple Access (TDMA)
- arguably the simplest amongst the three
- simple as it has quite a few rules for communication to take place
- strictly allocates and divides the resources among nodes
	- resources being divided up is **time**
	- used commonly by GSM

- each nodes gets access to the link in "rounds" $\implies$ can only do the transmission when it is the node's turn
	- each node gets a fixed time slot length in each round
	- $\text{Length of time slot = data frame transmission time}$
	- once we have fixed the # time slots for $k$ nodes, we will need to redesign the entire system or algorithm if there is a need to do so.

- some time slots could be idle when the nodes do not send data
	- at the end of each round (collection of $k$ time slots for $k$ nodes), the same thing starts again

- pretty straightforward, we just divide and allocate the time accordingly
	- each node cannot override or utilize a time slot reserved for another, even if they have no data to transmit.

![TDMA](../assets/TDMA.png)
- "Frame" is an overloaded terminology in this case, where it can refer to either the time frame allocated or the frame of data to be sent via physical link.

##### Properties
1. It is **collision free**: since there is an allocated time to transmit

2. It is **highly inefficient**
	1. unused slots go idle
	2. maximum throughput for a node is $\frac{R}{N}$, for $N$ nodes (regardless of whether each node wants to transmit or not)
		1. $= \frac{R}{N} \implies$ we have data to be transmitted
		2. $\lt \frac{R}{N} \implies$ we do not have data to be transmitted

3. It is **perfectly fair** since every node gets an equal amount of time each round to transmit

4. It is **decentralized**
	1. only coordination is to make sure the clocks of all nodes are synchronised

#### Frequency Division Multiple Access (FDMA)
- the channel spectrum is **sub-divided into frequency bands** and each node is assigned to a band
- multiple channels have data transmitting, but they do not interfere with one another
- unused transmission time in frequency bands go idle
- example: in FM radio (tune the radio to a particular channel or frequency) and satellite systems

##### Properties (exact same as in TDMA)
1. It is **collision free**: since there is an allocated time to transmit

2. It is **highly inefficient**
	1. unused slots go idle
	2. maximum throughput for a node is $\frac{R}{N}$, for $N$ nodes (regardless of whether each node wants to transmit or not)
		1. $= \frac{R}{N} \implies$ we have data to be transmitted
		2. $\lt \frac{R}{N} \implies$ we do not have data to be transmitted

3. It is **perfectly fair** since every node gets an equal amount of time each round to transmit

4. It is **decentralized**
	1. only coordination is to make sure the clocks of all nodes are synchronised


---
## C. Error Detection & Correction

### Motivation
- we are focusing on the underlying error-prone link
- when we send a datagram, the data being transmitted should carry some information which can be used for error-detection and checking.

### C1. Parity Bit Checks

### C2. Cyclic Redundancy Check (CRC)