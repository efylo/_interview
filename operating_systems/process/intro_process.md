# Process Management

## Abstract

A process is a program in execution. So, the process is considered 'active' entity, though the program is rather considered 'passive' entity. 

---

## Memory of a Process

The OS allocates the memory for a process if created. The memory have 4 partitions for specific purpose. 

1. **Text(Code)**

   A Process, including the Program Counter(PC)

2. **Data**

   Contains the global variable

3. **Heap**

   Dynamically allocated memory during run-time

4. **Stack**

   Temporary data - function parameters, return addresses, and local variables

---

## Attributes(Characteristics) of a Process

1. **Process Id**

   a unique identifier assigned by the OS

2. **Process State**

   ready, running, etc

3. **CPU registers**

   registers must be saved / restored in context switching

4. **Accounts information**

5. **I/O status information**

   devices allocated to the process, open files, etc

6. **CPU scheduling information**

   priority, etc

Each process have a unique Process Control Block(PCB), and above attributes are part of the PCB. 

### CPU and IO Bound Processes

If a process requires more CPU operations, then it is called CPU bound process. In similar way, if a process requires more I/O operations, then it's called IO bound process. 

---

## States of a Process

Introducing the state possible, 2^nd^ attribute from the above paragraph

1. **New**

   Newly created or being created process

2. **Ready**

   After creation, process becomes ready state - ready for execution

3. **Run**

   Process currently running in CPU

4. **Wait** (or **Block**)

   Process requesting I/O access

5. **Complete** (or **Terminated**)

   Process completed the execution

6. **Suspended Ready**

   When the ready queue is full - some processes move to suspended ready state

7. **Suspended Block**

   When waiting queue is full

---

## State Transfers

1. **Create**

   On creation, a process goes to the *Ready* state

2. **Run** / **Preempt**

   Process from *Ready* to *Run* state / from *Run* to *Ready* State

3. **Block**

   By I/O requests, from *Run* state to *Blocked* state

4. **Unblock**

   When I/O request completed, *Blocked* state to *Ready* state

5. **Terminate**

   When a process completed, *Running* state to *Terminated*

6. **Suspend** / **Resume**

   Between *Ready*/*Blocked* state and *Suspended* states

---

## Context Switching

The process of saving the context of currently running process and loading the context of another process. 

1. When a high-priority process comes to a ready state
2. An interrupt occurs (e.g. I/O request)
3. User and kernel-mode switch (not necessary)
4. Preemptive CPU sheduling used

### Mode Switch

Mode switch does not mean a change of the process. It occurs when system calls are made or faults occur. Though, context switch necessarily involves mode switch since context switch is done by the kernel mode. 

---

## Administrating

For use of context-switching, there exists a process table which saves information about processes. The information is called Process Control Block(PCB), which includes several data of the processes. 

Inside PCB, there are *pointer*, *process state*, *process number(PID)*, *program counter*, *register*, *memory limits*, *open files list*, etc. Page table is the table of PCBs, and the user(kernel) can access PCB through the unique PID. 

---

## Scheduler types

1. **Long-term** (performance)

   Decision on the number of processes in the ready state, which becomes the *degree of multiprogramming*. This decision lasts long time performance of the OS. 

2. **Short-term** (context switching time)

   Decision on the next executed process, which is called dispatcher. Movement of a process from the ready to the running state is called dispatch. 

3. **Medium-term** (swapping time)

   Swapping is quite different from context switching. It is the movement of a process from main memory to secondary memory, which is from the ready/blocked state to the suspended state. 

*Degree of Multiprogramming*

When the maximum number of processes that can reside in the ready state is 10, then the degree is 10. 

---

## Pre-emption

1. **Pre-emption**

   CPU can remove the process by force. It is also called as time sharing, or multitasking.  

2. **Non pre-emption**

   CPU cannot remove the process by force, processes run until the completion. 

---

## Reference

- [Introduction of Process Management](https://www.geeksforgeeks.org/introduction-of-process-management/)
- [States of a Process in Operating Systems](https://www.geeksforgeeks.org/states-of-a-process-in-operating-systems/)