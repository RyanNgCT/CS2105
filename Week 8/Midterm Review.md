### Question 1
The Internet is a network of interconnected hosts
- Q1. Option C is False, the Internet cannot be browsed (only www can be browsed)

Services running on the Internet include WWW and email.
### Question 2
- Multiple domain names may resolve to same IP address (Q2 Option B) $\implies$ see OTX AlienVault
- Root DNS only returns mapping of TLD DNS Servers, does not cache records
- For authoritative DNS, the structure and organization of the hierarchy is unknown

### Question 4
- imposes no limit on the length of the segment
- just cut based on the $x$ specified in `skt.recvfrom(x)`
	- segment greater than $x$, still received the segment

### Question 6
**Option 1: Non-persistent**
for the html file
- to establish the TCP connection we have $1 \times RTT$
- to get HTML file, we have $1 \times (RTT + a)$

for each of the objects
- to establish the TCP connection we have $5 \times RTT$
- to get all objects  file, we have $5 \times (RTT + b)$

**Option b: Persistent without Pipelining** (wrong as option but $6R$ instead of $7R$)
for the html file
- to establish the TCP connection we have $1 \times RTT$
- to get HTML file, we have $1 \times (RTT + a)$

for each of the objects
- to get all objects file, we have $5 \times (RTT + b)$

**Option c: Persistent with Pipelining**
for the html file
- to establish the TCP connection we have $1 \times RTT$
 - to get HTML file, we have $1 \times (RTT + a)$

for each of the objects
- for each packet, last bit takes $RTT + b$, wait until the HTML file is already received
- so it is $1 \times RTT + 5b$

Total is $3 RTT + a + 5b$

**Option d: Persistent connection with multiplexing**
- the amount of data is the same
	- transmission is still the same, just that smaller files can be transmitted faster
- similar to how option C is computed

**Option e: Multiple concurrent non-persistent connection**
for the html file
- to establish the TCP connection we have $1 \times RTT$
 - to get HTML file, we have $1 \times (RTT + a)$

for the objects
- establish multiple concurrent TCP connections is considered $1 \times RTT$ as well
- it is $1 \times RTT + 5b$ for the delay

### Question 7
- Option A: still have to establish the initial TCP setup (no change, still $12R + a + 5b$)
- Option B: have to wait for each object to come back before requesting the next (time taken is $8R +a + 5b$)
	- time taken is longer as we don't have concurrent connections
- Option C: TCP + HTML file + TCP (R) + HTTP object (R + b) $\implies 4R + a + b \lt 3R + a + 5b$, dependent on size of $a, b$

- Option E: non-persistent connection
	- need to establish TCP connection anyways, there is no change in the overall time in end end ($4R + a + b$)

### Question 9
- need to look at $A$ records to determine the IP address
- webmail here does not matter
### Question 10
- DNS is definitely used to change mapping from hostname to IP
- implies UDP is used as the transport layer
### Question 11
- nowhere does it say that `www.nus.edu.sg` in the request
### Question 12
- each segment max ($MSS = 1500$, the actual length $= 1500$)
- every packet can be $\leq 1500$B
### Question 13
- 