# Types of OS

## Abstract

An OS, do the basic tasks such as the management of files, processes, and the memory which can be called as the resource manager. Thus, it is an interface between the user and the machine. 

---

## Batch Operating System

Batch OS takes similar jobs of same requirements, group them into batches. The OS is reponsible for sorting jobs of similar needs. 

### Pros

- Processors know the time required for the job, though it is very difficult to guess how much time will take. 
- Multiple users can access, share
- The idle time is very small
- Ease in the management of repeated large works

### Cons

- Operators should be masters of batch sysems
- Hard in debugging
- Costly
- Wait time - if any job fails, other jobs have to wait

---

## Time-Sharing Operating System

Each task is given some time(quantum) so that the tasks smoothly works, a.k.a multitasking systems. OS switches to the next task if previous one uses all of given time. 

### Pros

- Equal in opportunity for each task
- Software duplication, CPU idle time is low

### Cons

- Problems on reliability, data communication
- The security and integrity have to be managed (of programs/data)

---

## Distributed Operating System

Quite recently developed, a system which interconnected computers communicate each other in the same network. Independent systems have their own resources, loosely coupled each other. Remote access to the files or software is possible in this OS. 

### Pros

- Failure of one system not affects others, since they are independent
- The data exchange speed increases
- Computation is highly fast and durable due to shared resources
- Load of host computers reduces
- Ease in scalability, systems can be easily added
- Delay in data processing reduces

### Cons

- Failure of the main network is fatal
- The language in distributed OS is not integrated
- Very expensive, highly complicated, not understood yet

---

## Network Operating System

Network OS, running on a server, provides the management over users, groups, security, applications, and some functionalities. They are also known as tightly coupled systems. 

### Pros

- Highly stable centralized servers
- Security concerns handled through servers
- Ease in integration of new technologies and hardware upgrades
- Remote access to servers is possible

### Cons

- Costly servers
- User depends on a central location for most operations(?)
- Regular demands upon maintenance and updates

---

## Real-Time Operating System

The response time, which is the time interval between requirement and reponse, is very small for Real-Time OSs. Real-time systems are used since their time requirements are really strict. Systems which small errors could be disastrous will probably require this type of OS. Some systems even not use virtual memory due to time constraints. 

### Pros

- Maximized consumption of device and system
- Time for task shifts are very less
- Focus on running applications, others are not really important
- Fit in embedded systems, since the programs are usually small
- Error-free
- Memory allocation

### Cons

- Limited tasks, only few tasks are applicable
- Heavy system resources, also expensive
- Complex algorithms
- Need for specific device drivers and interrupt signals
- Thread priority is not good for these systems

---

## Reference

- [Types of Operating Systems](https://www.geeksforgeeks.org/types-of-operating-systems/)

