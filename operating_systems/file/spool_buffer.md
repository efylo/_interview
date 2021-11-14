# Spooling and Buffering

## Spooling

SPOOL stands for *simultaneous peripheral operations on-line*. Spooling is a kind of buffering mechanism that the data to be used is kept, and executed by a device. Since peripheral equipments are so slow, there is more chance of a bottleneck, and the need of spooling is incremented. 

There exists a ready queue of jobs to be executed, which are executed in first in first out manner. 

### Application / Implementation

1. Inputs sent by a peripheral device is stored in spool, which are popped when ready. Consider the situation when a computer has stopped for the moment. The inputs you've put into the keyboard and mouse are done after a computer has resumed. Those inputs could be resumed since they are in the ready queue. 
2. A batch system also uses spooling, *batch* infers sequential features, so use of spooling in the batch system is normal. 

---

## Buffering

Buffer is some part of the main memory, which temporarily stores or holds the data. Buffering can help matching speed between sender and receiver. 

### Example

In early 2010's, the data transmission speed is quite slow. In my experience, watching a video on the internet generally makes lots of buffering maybe because the server of a video can't afford all requests from the clients, so that the data transmission speed of the server is quite slow. This makes buffering in the client's device, making user frustrated. 

### Difference

Spooling handles I/O of one job while computing for another job at the same time, though buffering handles I/O of only one job with its computation. So, it is possible to overlap jobs in spooling but not in buffering. Also, buffering is done through main memory, but spooling is not. 

---

## Reference

- [What exactly Spooling is all about?](https://www.geeksforgeeks.org/what-exactly-spooling-is-all-about/)
- [Difference between Spooling and Buffering](https://www.geeksforgeeks.org/difference-between-spooling-and-buffering/)