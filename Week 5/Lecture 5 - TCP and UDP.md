## A. Recap for Lecture 4
- Midterm topic up to transport layer, don't cover network layer
## B. Connectionless Transport: UDP
Packet is a very generic word, for every specific layer, we have a different terminology for the data
- Application $\implies$ message
- Transport $\implies$ segment
- Network $\implies$ datagram

- is a transport layer protocol, as specified in RFC 768 (documentation for UDP)
- for now, Google's QUIC uses UDP (need a library), but no need library to use TCP and UDP
#### Properties of UDP
1. adds very little service on top of the Internet Protocol
	- uses connectionless multiplexing and de-multiplexing (port numbering)
		- *multiplexing*: electronic process to allow $\geq 1$ electrical signal to be sent using one connection
			- can only differentiate using IP address + port pair
	- use of checksum

2. transmission in this case is unreliable
	- often used for streaming multi-media applications (which is loss-tolerant and rate sensitive)
	- reliability is as good as the network layer.

3. to achieve reliable transmission, the application needs to implement its own error detection and recovery mechanisms

**Caveat**
- if we send bytes that are too big, then it will be dropped ($\exists$ limit to the packet size somewhere)
- messages in UDP are read chunk by chunk
#### Socket Programming
- Internet is treated as black box by applications, just need to send inputs and receive outputs, through the use of sockets.

**Types of Sockets**
- Stream sockets (TCP) that utilizes TCP as the transport protocol (is connection-oriented and this reliable)
- Datagram sockets (UDP) that utilizes UDP (is connection-less and unreliable)
	- transmitted data may be lost, corrupted or received out of order

**Connectionless de-multiplexing**
*UDP sender creates a socket with a local port*
- create socket with local port no.
- when creating UDP datagram to be sent in socket, need to specify destination IP and destination port no.

*Transport layer receive UDP segment*
- check `dst_port` in UDP segment
- socket does not differentiate the origin port, directs all UDP segments to the addressed port number.
	- IP address is handled by the network layer, while transport layer handles IP address

UDP header format not tested, but have to know what are the header fields
- `src_port`
- `dst_port`
- `length`
- `checksum`

#### Checksum
- is a mechanism for error detection in transmission (how to detect corrupted packets)
	- checksum is an umbrella term for CRC, MD5, SHA1, SHA2 etc., as well as the UDP/TCP checksum in RFC 768

- guaranteed to detect single bit flips (does not guarantee $\geq 2$ bits and more)

**RFC 768 algo**
- Split into $16$-bit integers
- add all integers (`add`) on bit level, carry out is added again to each result (i.e. wrap around).

---
## C. Connection-oriented Transport: TCP

#### Properties of TCP
Is connection-oriented
- handshaking (exchange of control and negotiation messages) before sending application data

Reliable, in order byte stream
- app passes data to TCP
- TCP forms segments, while respecting maximum segment size

Flow & Congestion Control
- helps to prevent unnecessary losses

TCP is neither Go-Back-N, nor selective repeat
#### TCP Sockets
- is an interface 
- every connection is identified by the 4-tuple (`src_ip`, `src_port`, `dst_ip`, `dst_port`)

#### TCP segment structure
**Offset**
- offset is usually $\geq 5$ (if $\gt 5 \implies$ header is greater than $5 \times 32$ bits)
- denoted the size of where the data starts, relative to the no. of $32$-bit words.

**ACK Number**
- has ACK bit to indicate validity
- sends an ACK up to the missing byte, using the cumulative ACK model
	- indicates the *next byte* that the recipient has not yet received (if expecting the 6,000 byte then send ACK number as 6,000)

- similar to Go-Back-N, TCP sends the ACK of the earliest missing byte that is expected, even if later bytes have been received

- delay ACK scheme is usually used (after no new segments received after $x$ ms, then retransmit)

**Sequence Number**
- counts the **number of bytes**, not the segment number
- For the first $n$ bytes sent, then the sequence number is $0$

**TCP Echo Server**
- is full-duplex (i.e. bidirectional data flow)
- both users can send and receive data at the same time.
	- two way communication should be viewed independently ($A \to B$ has no relation with $B \to A$)

- starting sequence number is random to prevent attack
- the ACK piggybacks on top of the data
- ACK number should match with the sequence number

| 42  | 43  | 44  | 45  | 46  | 47            |
| --- | --- | --- | --- | --- | ------------- |
| H   | E   | L   | L   | O   | `<next_byte>` |
ACK of 47 is sent.

**Maximum Segment Size**
- determined by the link layer (how large the unit size can be)

**Retransmission**
- is done similar to Go-Back-N
- uses the oldest unACK-ed segment
- if ACK is lost, we wait for the duration of the timeout, then proceed to retransmit
- retransmitted data payload can be increased

**TCP Timeout value**
- timeout value is varied based on the $RTT$ value.
- If timeout is too short, then leads to premature timeouts and unnecessary retransmission
- Cannot be done using a normal average, but rather an Exponential Weighted Moving Average instead.

**TCP Fast Retransmission**
- have to compute the RTT, with respect to pipelines.
- Fast retransmission $\implies$ no need to wait for timeout before retransmission 

#### TCP Connection Establishment
- Client `SYN`, with initial sequence number $x$ (using a PRNG)
- Server `SYN-ACK`, with sequence number $y$ and `ACKnum` $x+1$ for return comms
	- ACK packet can contain data
- Client `ACK` with `ACKnum` $y+1$

**Attacks**
1. SYN Flooding (i.e. Denial of Service)
2. SYN-ACK Flooding (i.e. DoS to overwhelm network)
3. Reverse-ACK flooding
	- attacker uses victim's IP address as the "client"

#### TCP Connection Close
- send packet with the `FIN` flag to show connection teardown
- "I will not send any more data from my end"
#### TCP Flow Control
Host-to-host communications
- application may not read data in time (taking its own sweet time)
- enables buffered data into application
- can tell the sender how much to send using the receive window `rwnd` (decrements as TCP buffer becomes more and more filled).

- no need to know the details, but need to know the principles of flow control
#### TCP Congestion Control
Network Congestion
- being polite and send less if the network is congested
	- if there are packet lost then implement network control
	- reduce sending rate (lower rate of packet transmission)