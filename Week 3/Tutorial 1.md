Circuit Switching requires the link for the sender and the recipient to be up the whole time.

Packet switching $\implies$ Intermediate nodes need to receive the entire packet before sending it out again
- Queueing
- Processing
- Propagation
- Transmission: time needed to put data on the the physical link (i.e. electrical signals)

Throughput is a measure of end-to-end day (***Computation***: number of bits transferred per unit time)

Bandwidth is the maximum speed in which we can put data onto the data link.

Underlying transport layer protocol of HTTP?
- TCP

HTTP 1.0 versus HTTP 1.1
- one connection can be used to send multiple resources (or objects)
- in HTTP 1.1, we can send multiple objects simultaneously with pipelining

### Q1 a, b, c) Calculating Transmission and Propagation Delay
$d_{prop} = \frac{M}{s}$
$d_{trans} = \frac{L}{R}$
$d_{total} =  \frac{M}{s} + \frac{L}{R}$

#### Q1d)
The last bit just leaves Host A.

### Q1e, f)
$d_{prop} \gt d_{trans} \implies$ the first bit is flowing in the link and has not reached host B.

### Q1g)
$d_{prop} \lt d_{trans} \implies$ The first bit has already reached host B
- transmission delay is **not dependent** on propagation delay.
- $d_{prop} = d_{trans} \implies$ when last bit loaded, first bit already arrives at the other end.

### Q2) 
use the formula m/s = L/R
⚠️ Take note that question might provide data point in bytes instead of bits (requires conversion)


### Q3a) Calculating end to end delay
- Can ignore the others except for transmission (as stated in the question)

$\frac{8 \times 10^6}{2 \times 10^6} = 4$s

### Q3b) Time to hop through all 3 switches and reach the end host
- 3 hops, take the same queueing delay

$4 \times 3 = 12$s

### Q3c) 
1st packet: $10000 / 2 \times 10^6 = 0.005$s
2nd packet $0.005 \times 2 = 0.01$s

### Q3d)
first packet reach at 15msec
subsequent at 5msec

### Q3e)
- need to store and forward (packets behind need to wait for big packet to be processed)
- need to resend whole block if corrupt instead of small portion

### Q3f)
Recipient has to reassemble
More overhead needed (sender break up, recipient combine)
Packet Headers are also data $\implies$ take more time to be sent

### Q3g)
Minimum: $n-1$, cost effectiveness, has SPOF

Maximum $\frac{n(n-1)}{2}$ , more expensive, no SPOF

