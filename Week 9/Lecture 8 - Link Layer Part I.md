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
- Random access protocol: **No coordination** is occurring, Collisions are possible
- Taking Turns: Each person gets *some time* to speak
- Channel Partition: divide the channel into fixed smaller pieces
- Increasing complexity as we go down (i.e. we have more rules required)

- As engineers, we will have less complexity towards the bottom, as there is more order
	- collisions are harder to recover from while coordinating and implementing scheduled messages are easier

#### Ideal Multiple-Access Protocol
**Properties** (given a broadcast channel of rate $R$ bps)
1. *Collision Free*
2. *Efficient*: when only $1$ node wants to transmit, it can transmit at the **full rate** $R$.
3. *Fairness*: when there are $m$ nodes that want to transmit, each can send at average rate of $\frac{R}{m}$
4. *Fully Decentralised*: should not be a special node to coordinate transmissions (no central coordination required)
5. ⚠️ Mandatory Requirement: ==*no out-of-band signalling*==
	- *control signal and data* **goes through the same channel** (no using an external channel as a control path medium)
	- recover from all failures and errors on the **same channel**
	- principle of "don't use what is not allocated to you"
### B1. Random Access Protocols
- when node has something to send, just send (no need coordinate)
- random access protocols specify how to **detect** collisions and how to **recover from** collisions
- protocols should identify how much of the $L$ bits are the relevant data (cannot be exceeded or reduced)
- Slotted and Pure ALOHA is used for wireless communication in theory, but only pre ALOHA was put into practice
#### 1. Slotted ALOHA
- has a clock
	- time is divided into slots of **equal length** $\implies \text{length} = \text{time to transmit 1 frame} = \frac{L}{R}$ (transmission delay)
	- nodes only transmit at the beginning of a slot and time is synchronized at each node
	
- *no coordination* among nodes
	- is decentralised as we don't need any server. Only thing we need to **synchronize** or coordinate is the **clock cycles**

- break data into frames of size $L$ bits and only transmit at a certain time slot (usually $\lt$ MTU)
##### Operation
1. When have frame to send, wait until beginning of next slot and transmit the entire frame in the slot
2. No Collision $\implies$ transmission successful
3. Collision $\implies$ retransmit the frame again
	- *Issue:* What would happen if the frame sent by two nodes collide and then they retransmit again?
		- *Solution:* retransmission using "coin toss" with probability $p$ (so unlikely to retransmit and collide and the same time)
		- *Another Problem:* can retransmit for every time slot allocated

4. Slotted ALOHA algorithm will continue on until all nodes transmit the frames that they want to send successfully
![slotted-ALOHA](../assets/slotted-ALOHA.png)
##### Properties
- is *not* a *collision free* protocol
- it is **efficient** $\implies$ utilization is $100\%$ (i.e. use the entire bandwidth of $R$), assuming that only one node is active at a time
- if is not efficient when there are **many** active nodes transmitting (max efficiency $\approx 37\%$) $\implies$ slots will be wasted due to them being empty
- it is a perfectly fair protocol
- it is fully decentralised beside having to coordinate the clocks across nodes
#### 2. Pure / Unslotted ALOHA
- **no time slots** with no synchronization
	- a frame transmits immediately when it wishes to send data
- interference is generated when there transmissions beginning at between $t_0 - 1$ and $t_0 + 1$ and $t_0$ 
	- *probability of collision* has actually **doubled** as compared with Slotted ALOHA

	![pure-ALOHA](../assets/pure-ALOHA.png)
##### Operation
1. Send the entire frame
2. If no collision, assume data transmission is a success
3. If $\exists$ collision $\implies$ wait for 1 frame transmission time before retransmitting (happens until the entire frame is successfully transmitted)
	- like Slotted ALOHA, retransmission here is also done with probability $p$
##### Properties
- is *not* a *collision free* protocol
- it is **efficient** $\implies$ utilization is $100\%$ (i.e. use the entire bandwidth / has a throughput of $R$), assuming that only one node is active at a time
- if is not efficient when there are **many** active nodes transmitting (max efficiency $\approx \textbf{18}\%$) $\implies$ slots will be wasted due to them being empty
	- reduced efficiency as compared to Slotted ALOHA
- it is a perfectly fair protocol
- it is fully decentralised beside having to coordinate the clocks across nodes
##### Major Drawback of Slotted/Pure ALOHA
- cannot detect a collision 
	- all the nodes pay **no attention** to what is happening on the channel (i.e. if another node is transmitting at that point in time)

**How do you detect a collision?**
- when we hear someone else (receive something that you did not transmit)
- when there is $\gt 1$ signal (usually $2$)
- wait for someone to stop transmitting before (re-) transmitting
#### 3. Carrier Sense Multiple Access
- listen before transmitting (check if channel is in use, i.e. someone is transmitting on the medium)
	- sensed to be idle: transmit the entire frame
	- sensed to be busy: defer transmission until channel is idle again
- *still have the issue of collision* because of **propagation delay** on the rest of the nodes end when one nodes starts to transmit
- nodes continues to transmit even though it has detected the collision

#### 4. Carrier Sense Multiple Access / Collision Detection (CSMA/CD)
- detected by the network interface card
- don't transmit the remaining frame (time delay is for the jamming signal)
	- jamming signal to alert other nodes of collision

- the retransmission probability should keep decreasing
	- However, probability of collision stays the same
	- we can reduce the probability further on each round of collision
		- **exponential backoff** (unlike Slotted ALOHA which is linear backoff - sorta)
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
	1. We *cannot fully obtain* the bandwidth $R$

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
- we are focusing on the underlying **error-prone link**
- when we send a datagram, the data being transmitted $D$ should carry some information which can be used for **error-detection** and checking (and possibly correcting the error)
	- no guarantee that whatever is transmitted will be delivered

- receiver may receive $D'$, i.e. not the full and correct version of $D$.
	- receiver has to make a decision whether to accept and forward the packet up to the network layer **if no error detected** or discard the packet (if $D \neq D'$)
	- as a result, we want to have an error detection scheme that reduces the chances of missing the error

- error detection should be **probabilistic**

- Goal (quite impossible): achieve reliable data communication over an inherently unreliable network medium
![error-detection-model](../assets/error-detection-model.png)
- Error detection schemes are **not 100% reliable**

**Trivial Error Detection**
- copy and send the same exact data as a contiguous block right after the data itself
	- we send $2n$ bits instead of $n$
	- chop into two halves and then do the error checking (bit-by-bit comparison)

### C1. Checksum (recap)
- treat the segment contents as a sequence of $16$-bit integers
- perform $1$'s complement on the sum of segment contents
### C2. Parity Bit Checks
- underlying principle is to detect half the errors
#### Single bit parity
- Notation: $D \implies$ the whole data segment to be sent, $d\implies$ **# bits** to be sent or transmitted
- want to ensure that # bits set to $1$ is **even**
	- if not so, we augment or "pad" the number of bits such that it fulfils the even criteria

- sender simply includes one additional bit
	- For **Even Parity Scheme**
		- if total # $1$s (set bits) is even, then set parity to $0$
		- if total # $1$s (set bits) is odd, then set parity to $1$ 
		- choose the value s.t. total # of $1$s in the $d + 1$ bits is **even**

- good for **detecting single bit errors** in data
	- detects an odd number bit flips (total # $1$s in the bit counts increasing or decreasing)
	- cannot detect an even number of single bit flips or error

- it works exceptionally well mathematically
	- probability of multiple bit errors if low, assuming that these errors are independent (for $n$ bits, we have $\frac{1}{2^n}$), which is **not true** in reality
	- errors are *clustered together in bursts* (unable to detect, depending on the length of the bursts
		- $P(\text{Undetected}) \cong 50$
#### 2D parity
- single bit parity is the basis for defining two-dimensional parity
- we arrange the data as a matrix of $i$ rows and $j$ columns
- we generate parity for each of the rows and columns separately
	![2D-parity](../assets/2D-parity.png)

- we will obtain $i + j + 1$ parity bits in total
	- resultant $i + j + 1$ parity bots comprise the link-layer frame error detection bits.
	- corner parity bit is generated based on column and row parities

- we should use the same parity scheme across all rows and columns (decide on whether we want to use odd or even parity)

**Properties**
1. Can **detect and correct** single bit errors in data (up to one bit)
	1. using the $i^{\text{th}}$ row $j^{\text{th}}$ column bits (pinpoint the location and flip the bit to the correct one)

2. Can **detect** any two bit error in data (but cannot correct)
	1. can detect parity errors at two rows or two columns
	2. there is no unique way to fix the error (possible overlap with correct bits)

3. Overhead associated with sending the parity together with the data as well.
	1. cost of taking up some space as part of the MSS
### C3. Cyclic Redundancy Check (CRC)
- very much *misunderstood* error detection scheme
- simplistic and efficient
#### Motivation -- The Problem
Assumption that we wish to transmit **non-binary data** $D$, without any error to the receiver
- $D$ is a $d$ digit number is augmented by $R$ which is the checking code, of **size** $r$ digits, where $d, r \gt 0$
- $R$ is the *augmented data* known as the EDC, or ***Error Detection and Correction bits***
- **Constraint:** 
	- small number of addition bits to be transmitted
	- generate the checking bits $R$, s.t. the sender can compute $R$ easily though the checking algorithm
	- make sure that the receiver can also **easily verify** the integrity of $D$, through the use of $R$ (errors should be easily detectable by the recipient)
#### Motivation -- The Solution
- consider the mathematical properties of division (remainder and quotient)
	- we shall use a special $r$-digit (of size $r$) number $G$, known as the Generator.

- using modulo arithmetic by $k$, where $D \geq k$, we observe that there can be bit flips that result in the check matching.
- every number sent by the sender is guaranteed to be divisible by $G$ (see CS1231S divisibility property)
	- each number is a multiple of $7$
	- both of what is send looses the original data
