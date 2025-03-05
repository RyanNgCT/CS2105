## Subnets and Hierarchical Addressing
- hosts in subnet can communicate with each other without using an intervening router
- upper router needs to store all the hosts in the subnets that it doesn't even below to in its routing table
## NAT
- distinguish hosts within the subnet with a random port mapping
- solves the issue of not enough IPv4 addresses
## Overhead
- headers etc, like non-payload and non-data records
- IP segment consists of $20$ bytes for IP, $20$ bytes for TCP and $40$ bytes for application data
## Subnet Mask
Example IP Address and mask of `16.27.24.0/26`
- all address have the address of `16.27.24.00XXXXXX`, where $X \in \{0, 1\}$

Can combine the blocks together by assigning a new network address prefix
## Network Prefixes
- which are the IP addresses that fall inside the block `192.168.56.128/26`
	- essentially is inside the range `192.168.56.10000000` to `10111111`
	- convert back to decimal to obtain decimal representation of IP address

- how to split up a block
	- note the number of subnets required
	- in this case, we require $4$ subnets (i.e. $2^2$) $\implies$ always round up the number to the nearest $2^n$

**Subnets:**
- `192.168.56.1000XXXX`
-  `192.168.56.1001XXXX`
-  `192.168.56.1010XXXX`
-  `192.168.56.1011XXXX`
- length of the network prefix is not `/28`, up from `/26`
## Prefix Matching
- based on the prefix network bits, we decide the blocks or range where we can forward them to
- Otherwise classification $\implies$ can subtract the blocks from $2^8$ for the hosts bits
$$
\text{Otherwise} = 2^8 - 2^a - 2^b - 2^c
$$
## Private IP Addresses
- can be used without coordination from an Internet registry (is not globally unique)
	- basically, need to go though IANA to acquire the IP address blocks
- Canvas uses public IP since we require coordination from the Internet registry
