## Motivation
- need to retrofit the TCP/IP protocol stack with security
- we assume that everyone is a good guy (no interest in manipulating or disrupting communications between parties)
- make sure we have a TCP/IP Client-Server program

**Conditions**
Need to provide countermeasures for the following problems
1. Eavesdrop $\implies$ compromise of Confidentiality (your data stays private, $3^{rd}$ parties cannot understand)
2. Delete/Modify/Add messages $\implies$ compromise on Integrity
	1. We cannot control the channel (the intermediate nodes), but we can **detect** modifications
3. Impersonation (Authentication)
4. Compromise on Repudiation (Authentication)

![security-problem](../assets/security-problem.png)
Security is implemented at any layer of the network stack.
- DNS and IP level has inherently no security baked in (need to have a consideration for this)

**What can attackers do**
- eavesdrop
- insert messages
- hijack
- denial of service

Good Security is about risk management

### Cryptography
- Confidentiality: if code language is secret, the MiTM cannot understand it
- Authentication: if code language is secret, only Alice and Bob can write it
- Integrity: If the code language has an inviolable property

- creating a "secret" language

- Abuse of Notations: need to be clear which is the key and which is the algorithm (for encryption)
	- encryption $\to \times$
	- decryption $\to \div$

**Things to agree on** (even though we are using a public channel, we need our communications to be private)
- encryption and decryption algorithm
- the keys which they use

### Symmetric Encryption
- Key exchange (distribution) is a problem