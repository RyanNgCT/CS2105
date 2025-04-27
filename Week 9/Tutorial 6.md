h#### Question 1a) Give an example IP address assignment to all interfaces in this home network.
![tut6-q1](../assets/tut6-q1.png)

- Router Internal: `192.168.1.1`
- PC 1: `192.168.1.2`
- PC 2: `192.168.1.3`
- PC 3: `192.168.1.4`

#### Question 1b) Suppose each host has two ongoing TCP connections, all to port `80` of a server at `128.119.40.86`. Provide example corresponding entries in the NAT translation table.
![tut6-q1b](../assets/tut6-q1b-NAT-table.png)

❌**WAN side should be using `24.34.112.235`**
Ports within LAN side, within each host have to be unique
#### Question 2) Consider sending a 1500-byte IP datagram into a link that has an MTU of 500 bytes. Suppose the original datagram is stamped with the identification number 422. Also assume that IP header is 20 bytes long.

#### a) How many fragments will be generated?
1500 Byte IP datagram consists of **20 Byte Headers and 1480 Byte Payload**

$$
\begin{aligned}
\text{MSS} &= 500 - 20 = 480 \\\\
\text{\# fragments generated} &= \frac{1480}{480} = 3.08333\ldots \approx \boxed{4} \text{ fragments}
\end{aligned}
$$
#### b) What is the length of each fragment (including IP header)?
$$
\begin{aligned}
\text{Length of Fragments 1 to 3} &= 500 \text{ bytes each} \\
\text{Length of Fragments 4} &= 20 + (1480 - 480 \times 3) \\
&= 60 \text{ bytes}
\end{aligned}
$$
#### c) What are the values of identification number, offset and flag in each fragment?
$$
\begin{aligned}
\textbf{Fragment 1:} \\
&\text{ID Number: } 422 \\
&\text{Offset: }  0 \\
&\text{Flag: } 1 \\\\
\textbf{Fragment 2:} \\
&\text{ID Number: } 422 \\
&\text{Offset: }  480 \div 8 = 60 \\
&\text{Flag: } 1 \\\\
\textbf{Fragment 3:} \\
&\text{ID Number: } 422 \\
&\text{Offset: }  60 + (480 \div 8) = 120 \\
&\text{Flag: } 1 \\\\
\textbf{Fragment 3:} \\
&\text{ID Number: } 422 \\
&\text{Offset: }  120 + (480 \div 8) = 180 \\
&\text{Flag: } 0
\end{aligned}
$$

#### Question 3) The following diagram shows a simple network topology with 4 nodes. The links in the diagram are labelled with the cost of each link. The nodes run distance vector routing protocol. The protocol has terminated, and each node knows the cost of the minimum cost path to every other node.
- Initial Routing Table: only know about cost of direct links
![tut6-q3](../assets/tut6-q3.png)

#### Question 4i) Within the IP packet header, what is the value in the upper layer protocol field?
![tut6-qn4](../assets/tut6-qn4.png)

![tut6-qn4i](../assets/tut6-qn4i.png)

A: `ICMP`
#### Question 4ii) Which fields in the IP datagram always change from one datagram to the next within this series of ICMP messages sent by your computer?
look at the request fields only
- ID field is unique for every packet that is not fragmented!
A: `Identification`, `Header Checksum`

`Flags` and `TTL` (???)

---
## Lecture Recap
### 1. Longest Prefix Matching 
- router will look at the destination IP's prefix and forward it to the corresponding interface
- we will choose the longest prefix and forward the packet based on the interface with the longest IP prefix

### 2. Routing Algorithms
- RIP runs over UDP and provides a service to IP, but it still runs over the Network Layer.
- If no updates received from direct neighbour after $180$ seconds $\implies$ link is down, populate routing table with $\infty$

### 3. ICMP
- used to implement `ping` (reachability) and `traceroute` (returns all the intermediate hops along the way)

### 4. Network Layer Service Model
- is a best-effort service model, without speed, timing and reliability guarantees.
- No bandwidth and throughput guarantees as well.

### 5. IP address assignment
- cannot assign
	- `192.168.0.0` (reserved to denote the address of the whole network itself)
	- `192.168.0.255` (broadcast)