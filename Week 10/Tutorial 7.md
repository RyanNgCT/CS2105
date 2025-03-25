## Lecture Recap - Link Layer
- concerned with sending packets to adjacent nodes over a single link

**Types of Network Links**
1. Point to Point
2. Broadcast Link
	1. has multiple nodes along the link and all messages are sent on the link received by all nodes

**Types of Protocols (8 Types)**
1. Random Access $\implies$ Slotted ALOHA, Pure ALOHA, CSMA, CSMA/CD
2. Taking Turns Protocol $\implies$ Polling, Token Passing
3. Channel Partitioning $\implies$ Time and Frequency Division Multiple Access

**Comparing Multiple Access Protocols**
- given a full broadcast channel rate (bandwidth) of $R$ bps
- we have four desired properties (for our protocol to fulfil)
	- collision free
	- efficient
	- fair
	- decentralized

**Error Detection & Correction**
- two different types of schemes for parity $\implies$ even and odd parity schemes
	- even parity, add extra bit to ensure total # $1$s is even
- $2D$ parity scheme
- CRC

---
## Tutorial Questions

### Question 1
- assume all links are reliable
- is TCP redundant?
	- it is not redundant
	- packets still could be reordered
	- data loss can still occur:
		- but not along the links (when router buffer is full, packet is dropped $\implies$ occurs in the network layer instead)
		- TTL set to $0$ eventually

- possible that packets take different paths to reach the receiver, so they can be received out of order
	- TCP will help to buffer the packets until all packets are in order
	- need TCP to help recover from data loss

### Question 2
In CRC, we have $3$ binary numbers
- $D$: data
- $G$: generator of length $r+1$ bits, known to both sender and receiver
- $R$: CRC of length $r$ bits, to be determined by the sender

- Modulo two division $\implies$ bitwise XOR on blocks of $4$ binary digits

- In general, don't need to keep track of the digits on the top (quotient sort of)
Answers: (a) $110$  (b) $011$ 
### Question 3a
- assume even parity
- all the parity bits in the row and columns are zeroes
### Question 3b
- can tell where the bit error occurred, then just flip to correct it (for any singular bit in the data array)
### Question 3c
- can just take any two contiguous bits in the same row or column (for detection of two bits)
- every single two bit error can be detected, but cannot be corrected using 2D parity
### Question 3d
- consider a square within the matrix, when all the bits flip, the parity check will still pass $\implies$ i.e. no detection of errors

### Question 4
- Key Concept: **Multiple Access protocols**
- CSMA: nodes will transmit the moment that they detect that the channel is available (delay the transmission otherwise)
	- if collide, keep transmitting
	- if data is garbled, then we discard

- consider TDMA: most nodes will transmit frequently
	- how much of the link is being used to transmit useful data?
	- utilization is probably going to be high

- consider CSMA: lots of collisions (utilization will be low)
	- time spent transmitting will be wasted because the data will likely be garbled

- consider token passing: no collisions (so suitable from a utilization POV)
	- all of the time will be used to transmit useful data
	- may not be suitable because there are many possible points of failure
### Question 5
- bit time: is the time taken to transmit $1$ bit on the link itself
- $B$ can start transmitting between $t=0$ and $t = 245$ under CSMA/CD.
	- $B$ can only **detect that the channel is not free** when the first bit of the packet sent by $A$ is received by $B$
	- the latest time that $B$ can send is at $t = 244$

- $t = 512$ is the earliest time that $A$ will start transmitting because of transmission delay (by size of the MTU)