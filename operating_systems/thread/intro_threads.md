# Threads

## Abstract

Thread is a path of execution within a process. A process can hold multiple threads. Thread is sometimes called a lightweight process, it is usually used to achieve parallelism. Possible example is multiple tabs in the Google Chrome, multiple documents in Adobe Acrobat DC. 

---

## Resources

Threads have shared resources as well as independent resources on their own. 

### Shared Resources in Threads

- Code, Data section / OS resources, Shared memory space

### Independent Resources in Threads (Local)

- Program Counter(PC), Register set, Stack space

---

## Advantages

1. *Responsiveness*

   The output of a thread immediately returns if completed. 

2. *Faster context switch*

   Context switch time is lower than the one of process's (Less overhead)

3. *Effective utilization of multiprocessor system*

   Scheduling multithreading process within multiprocessor system makes execution faster. 

4. *Resource sharing*

   Shared resources can be effectively used. 

5. *Communication*

   Processes need IPC to communicate, though threads need not. 

6. *Enhanced throughput of the system*

   Considering thread as a job, this enhances throughput. 

---

## Types

1. User-level threads

   Implementing threads in high-level language is mostly user-level threads. The OS does not know about how a process uses user-level threads. They are also easy to implement, since high-level languages mostly have threading modules. Since they don't need system calls, context switch is less costly. Threads that are dependent each other are user-level threads. Since a process controls the threads of its own, block of a thread causes entire process to halt. 

2. Kernel-level threads

   They are the threads implemented by the OS. They require quite a complex implementation, need OS support. Though, they are independent each other and other threads is not blocked even though one thread is blocked. 

Two types of threads interact in-between the OS. There exist three models upon how they interact each other. Referring to their relationships, the models are

1. Many to Many Model

   Multiple user-level threads are executed upon multiple kernel-level threads. 

2. Many to One Model

   Multiple user-level threads are executed upon a single kernel-level thread. 

3. One to One Model

   A single user-level thread is executed upon a single kernel-level thread. Block of a user-level thread correspondes to the block of a kernel-level thread in this model. 

---

## Reference

- [Thread in Operating System](https://www.geeksforgeeks.org/thread-in-operating-system/)
- [Difference between User Level thread and Kernel Level thread](https://www.geeksforgeeks.org/difference-between-user-level-thread-and-kernel-level-thread/)
- [Multi Threading Models in Process Management](https://www.geeksforgeeks.org/multi-threading-models-in-process-management/)