Finals Cheatsheet allowed, double sided
4 Assignments, Programming Style
- have to follow the textbook for material, not so up to date (i.e. advanced courses)
### Communications
- computer networks and postal services are cross-globe communication services
- work over different medium
- seamless abstractions (inner-working of networking abstracted away from users)

### Why the Internet
- something that we need for survival
- is our connection to the world

- made by US unis, later onto US Dept of Defense
	- to ensure that maintain communication during nuclear war
	- made to have reliable redundancy

- ARPANET - Early form the the Internet
### Properties of the Internet
- Note that Internet $\neq$ World Wide Web

- The Internet consists of multiple services, whereas WWW is one of the services. Internet is a network of connected computing devices.

- The Internet is a type of infrastructure (to connect hosts or endpoints together), not a service
	- **Network Edge** consists of hosts, servers, Smart devices etc.
	- **Network Core** consists of ISPs, Routers, etc.

- Hosts run network applications
	- Web: browsers $\leftrightarrow$  web servers
	- Games: clients $\leftrightarrow$ game servers
	- VoIP: IP phones $\leftrightarrow$ PBX Servers
	- BitTorrent (P2P): peers $\leftrightarrow$ trackers

### Protocols
define the:
1. **format and order** of messages exchanged amongst entities $\implies$ parties need to conform to the standards set out in the IEEE specification
2. **actions** taken upon receiving the messages

E.g. Used to have snail mail to deliver catalogues (place in envelope and send it back)

Protocol Examples
- HTTP, FTP, SMTP, TCP, RTP

Someone (ISP) need to provide hosts with an **access network** they can access the Internet $\implies$ Internet conduits, cell towers (i.e. the infrastructures)
- residential access networks
- institutional access networks in schools and corporations
	- typically used in companies, universities etc.. $\implies$ bandwidths in Mbps and Gbps
- mobile access networks

---
## Network Core
- we have a mesh of interconnected routers
- Fundamental qn: how is data transmitted

### Circuit Switching
- between each node, need to allocate resources and the nodes in between them must be up for the entre duration
- call setup is required

### Packet Switching
- every node makes the **best effort** to deliver the packet $\implies$ only deal with one packet, no resource allocation needed
- router routes things using the store and forward or routing and addressing techniques
- is used by the internet

- resources are used on demand
- excessive congestion is possible (send through much traffic to router $\implies$ but there are techniques to mitigate congestion)

#### Store and forward
- packets are passed from one router to the next
- entire packet must arrive before it can be transferred

### Internet Core
- Tier 3 - ISP / Telcos (which are access ISPs)
- Tier 2 - Global ISPs (using undersea cables) $\implies$ using Internet Exchange Points (IXP)
- Tier 1 - Big Companies like Akamai, Google etc.


- Autonomous Systems are an organization of networks each owned by an organization

### Rules of the Internet
- Autonomous Systems have various organizations
	- Singapore Network Information Centre
	- Internet Society (ISOC)
	- Internet Engineering task Force (IETF)

---
## Delay, Loss and Throughput Networks
- how is network speed measured 
	- what does it mean by faster $\implies$ water pressure? or volume of water?

### Packet Loss
- the packets will queue in router buffers (to wait for their turn to be sent out one by one)

### Packet Delay
1. Singular Nodal Processing: time to read the packet and where to send the packet to (processing delay)
	1. "check the bucket"
2. Once it is determined, then the packet will queue (queueing delay)
	1. "wait for turn"
	2. delay at the end
3. Transmission Delay (10 Mbps): time taken for entire packet to be transmitted from one router to another
	1. The medium determines how much you can stuff into the cable
	2. "time taken to pour into pipe"
4. Propagation Delay: Time taken for one bit to travel through the medium to the other end (speed of light)
	1. "time taken to travel across pipe"

### Throughput
- how many bits can be transmitted per unit time
- measured for end-to-end communication
- different links may have different link capacity


- we use metric units to measure throughput (principal metric prefixes)
---
## Protocol Layering and Service Models
- each protocol layer provides a different service
- one container TEU $\implies$ used for shipping

- Internet uses packages as well