# Multiple-Processor Scheduling

## Abstract

Multiple-processor scheduling is inevitable in an environment with mutiple CPU. There is a need for load-balancing to each queue for effective use of the resources available. 

There are many ways to solve multiple-processor scheduling. One of them is to use a **master server** that presides all decisions of scheduling and I/O requests. Other servers or processors are able to execute the processes only in user mode. Using a master server is called **assymetric multiprocessing**. 

Another approach is **symmetric scheduling**. Where each processor can self-schedule on its own. There is a common queue, with each ready queue inside each processor. Each processor can have their own scheduling algorithm, making decision on their own. 

---

## Processor Affinity

Affinity between the processor and processes denotes that they are friendly to each other. Since each processor checks for cache memory to check if the process is available, it is costly to use the process in cache memory of other processors. For symmetric scheduling, the processors try to keep running the process on their cache memory. This is called processor affinity. 

Soft affinity denotes an operating system that does not guarantees a process to run on the same processor, and hard affinity is not. Changing how an operating system will work is possible in Linux. 

---

## Load Balancing

In symmetric multiprocessing system, load-balancing is the word to denote that the load is evenly distributed to all processors. It is only necessary for the system where each processor possesses its own private ready queue. 

**Push Migration** and **Pull Migration** is possible way to implement load balancing. Push migration is the mechanism that pushes load of busy processors to idle or less busy processors. Pull migration is the mechanism where idle processor pulls the task from a busy processor. 

---

## Multicore Processors

Similar to multi-processors, but multicore means that the processors are placed within the same physical chip. They are faster and consume less power, though it is more complicated to schedule them. 

General issue in multicore processors is **Memory Stall**. They refer the processor spends lots of time waiting for the data not in the memory. There are many reasons, though generally cache miss makes this problem. They can be solved through multithreaded-core processors. Processor still works even though one thread is in memory stall, just lessens performance of the overall processor. 

---

## Virtualization and Threading

They refer a single CPU system acting like multiple-processor system. Though, they result in poor performance. 

---

## Reference

- [Multiple-Processor Scheduling](https://www.geeksforgeeks.org/operating-system-multiple-processor-scheduling/)