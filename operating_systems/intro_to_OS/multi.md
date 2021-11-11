# Multi

## Programming

A computer running more than one program at a time. 

Multiple processes are waiting to be executed inside job pool. CPU then dequeues a job, loads into main memory and executes it. The execution is interrupted by some external factor or request for I/O. 

In multi-programmed system, CPU never becomes idle. For example, when a job A is requested and gone for I/O task, the OS choose a job B to be then executed. Since I/O tasks usually takes much more time than CPU tasks, this surely increases effective use of the CPU. 

---

## Tasking

Tasks share a common resource (like sharing a CPU). 

Tasks can refer processes, programs, threads, etc. It's like me editing markdown files on the Typora, surfing geeksforgeeks through the Google Chrome, while listening to Lo-Fi musics through Youtube lives. 

Thus, multitasking can be considered as a logical extention of multi programming. Since multi programming purely considers context switching techniques, while multitasking is not. 

Time quantum given to the processes are so small, that humans think that processes are running simultaneously. 

---

## Threading

An extension of multitasking. 

A thread is a basic unit of CPU utilization, which is smaller than a single process. Processes can have multiple threads (code segments). Multi threading of a process is the ability that a process can manage more than a user at a time, process multiple requests of the same user, within a single program. 

Multi threading can lead to increased responsiveness, since the block of one thread does not halt the program down. Also, there is no burden in creating and allocating if you use multi threads. So, burdens are less costly in multi threading. 

---

## Processing

A computer using more than one CPU at a time. 

By understanding CPU as a processor, multi-processing could be understood as multiple processors, CPUs is used within a computer system. Since multiple processors are physically available, multiple processes can be done at a time. The processors share the computer bus, (sometimes the clock, memory, and peripheral devices). 

Computing power increases by the number of processors. Also, failure in a processor does not make the computer to halt, which makes the reliability increased. 

Multiprocessing is hardware-level considerations, though multiprogramming is the consideration on keeping several programs in main memory, executing them concurrently in a single CPU. 

---

## Reference

- [Difference between Multiprogramming, multitasking, multithreading and multiprocessing](https://www.geeksforgeeks.org/difference-between-multitasking-multithreading-and-multiprocessing/)