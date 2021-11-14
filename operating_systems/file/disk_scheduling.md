# Disk Scheduling Algorithms

## Abstract

The OS schedules I/O requests that arrives for the disk. Disk scheduling is inevitable since multiple I/O requests can happen, some requests can be located far from each other, and the disk is the slowest component of a computer. 

---

## Key Factors

- **Seek Time**: Time taken to locate the disk arm to a certain data
- **Rotational Latency**: Time taken to rotate a certain sector of the disk
- **Transfer Time**: Time to transfer the data - depends on the rotating speed, number of bytes
- **Disk Access Time**: *Seek time* + *Rotational latency* + *Transfer time*
- **Disk Response Time**: Average time spent by I/O requests, also can be measured by *Variance*

---

## Disk Scheduling Algorithms

1. **First Come First Serve** (FCFS)
   - *Pros*: a fair chance, no indefinite postponement
   - *Cons*: seek time not optimized, may not be the best
2. **Shortest Seek Time First** (SSTF)
   - *Pros*: average response time decrease, throughput increase
   - *Cons*: overhead in calculating seek time, starvation possible, high variance of response time
3. **SCAN** (a.k.a *elevator algorithm*)
   - *Pros*: high throughput, low variance, average response time
   - *Cons*: long waiting time for certain locations
4. **CSCAN** (Circular-SCAN)
   - *Pros*: wait time more uniform than SCAN
   - *Cons*: -
5. **LOOK**
   - SCAN moves until the end of the disk, while LOOK moves until the last request
   - so, slightly faster than SCAN
6. **CLOOK** (Circular-LOOK)
   - Moves from the last request to the first request, no traversal to the end of the disk
7. **RSS**
   - random scheduling, algorithm is perfect when there are random attributes
8. **Last In First Out** (LIFO)
   - *Pros*: maximize locality, resource utilization
   - *Cons*: a little unfair algorithm, starvation possible
9. **N-STEP SCAN**
   - use a buffer of N requests, which are processed at once
   - *Pros*: no starvation
10. **FSCAN**
    - use of two sub-queues, the first queue serviced during the scan, new inputs to the second queue
    - *Pros*: FSCAN & N-STEP SCAN prevents arm stickiness

---

## Reference

- [Disk Scheduling Algorithms](https://www.geeksforgeeks.org/disk-scheduling-algorithms/)