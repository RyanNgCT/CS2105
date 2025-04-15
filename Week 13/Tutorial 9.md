### CIA Triad in Network Security
1. Confidentiality $\implies$ only sender and receiver should understand the message
 2. Integrity
3. Authentication $\implies$ ties into non-repudiation as well
### Encryption
**Procedure**
- Sender encrypts plaintext using encryption algorithm $K_A$
- Receiver decrypts ciphertext using encryption algorithm with $K_B$

**Types**
- symmetric key crypto: both hosts need to agree on the symmetric key $K_S$
- asymmetric key crypto: $K_A$ and $K_B$ are distinct.
### RSA Mathematics
- public and private keys generated using two large prime numbers
	- tuple of two numbers $(n, e)$ and $(n,d)$

- take plaintext and raise to power of prime to obtain ciphertext

---
### Question 1 - Substitution Ciphers
- the key is the mapping between the letters
### Question 2 - Keys
- suppose $N$ people each want to communicate with $N -1$ people
	- no one else should be able to understand the message
	- have the option to use either symmetric or non-symmetric key

- $K_S$ has to be unique for every pair of users $A$ and $B$ within the $N$ number of people
	- $\#(A, B) \implies \begin{pmatrix}N \\ 2\end{pmatrix} = \frac{N(N-1)}{2}$ keys

- In public key cryptography, $A$ encrypts message with $K_A^+$ and $B$ decrypts the message with $K_B^-$
	- total of $2N$ keys
### Question 3
Mappings:
- `l` $\implies 12$, `o` $\implies 15$, `v` $\implies 22$, `e` $\implies 5$
- encrypt: $c = m^e$ mod $n$ (do it character wise)
- decrypt $m = c^d$ mod $n$
### Question 4
- designing a $128$-bit block cipher
- how many possible # input blocks: $2^{128}$ distinct blocks
- how many possible mappings are there $\implies$ ways to permute $2^{128}$ blocks is $2^{128}!$ mappings
- if we view each mapping as a key how many possible keys do we have? $\implies 2^{128}!$ 
- Why is AES able to function with $128$-bit key? $\implies$ brute forcing $2^{128}$ is hard enough to break (sufficiently strong)
	- each key defined a random permutation