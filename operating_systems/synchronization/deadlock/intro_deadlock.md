# Deadlock

## Abstact

Deadlock occurs when a set of processes each is waiting for another process to end while possessing their own resources. For example, assume there exist 3 processes A, B, C. A is waiting for B's resource, B for C's, and C for A's. Then, no process can ever acquire the resource they are waiting for. 

---

## Conditions

Deadlock happens only when four conditions are met, which are

1. *Mutual Exclusion*: Only one process solely use the resource itself. 
2. *Hold and Wait*: A process holds the resource, waits for the other. 
3. *No Preemption*: A process cannot preempt other's resource.
4. *Circular Wait*: A set of processes have to wait each other in circular form. 

---

## Solution

Three solutions are possible to get rid of deadlock, which are

1. *Deadlock prevention / avoidance*

   By negating only one of the above conditions. Avoidance through ensuring all information about resources are known, e.g) Banker's algorithm. 

2. *Deadlock detection and recovery*

   Solve the deadlock through preemption when happens. 

3. *Ignore the problem altogether*

   If deadlock rare, just ignore the problem and when it happens, just reboot. e.g) Windows, UNIX

---

## Deadlock Detection and Recovery

1. When a graph of the processes are cycle. (Circular wait)
2. 1^st^ condition is suffiecient, but not necessary. 
3. If happens, then kill the process or preempt the resource

---

## Deadlock, Livelock and Starvation

Livelock is somewhat different from deadlock. Deadlock is a loop of endless waits, but livelock is a loop of endless running without progress in the processes. So, livelock can be considered as a kind of starvation. While processing multiple processes without progress, other processes will never get a chance to execute. 

---

## Deadlock Prevention

1. *Elimination of Mutual Exclution*

   Not possible since it obeys the concept of multi processing. 

2. *Elimination of Hold and Wait*

   Allocate required resource before the start of execution. Though, there are problems about low device utilization, starvation. 

3. *Elimination of No Preemption*

   Preempt resources by higher-priority processes. 

4. *Elimination of Circular Wait*

   Request resource in an order. The next resource requested by certain process must be next to the resource it currently uses. 

---

## Deadlock Avoidance (Banker's Algorithm)

Banker's Algorithm tests all the request if it is safe or not. The request is not allowed if it is considered not safe. 

Banker's Algorithm needs, 

1. Maximum need of resources by each process
2. Currently allocated resources by each process
3. Maximum free available resources in the system

Request is considered safe when, 

1. If the request of the process <= maximum need to that process
2. If the request of the process <= available resource in system

Though, deadlock prevention is more strict than avoidance. 

---

## Reference

- [Introduction of Deadlock in Operating System](https://www.geeksforgeeks.org/introduction-of-deadlock-in-operating-system/)
- [Deadlock Detection And Recovery](https://www.geeksforgeeks.org/deadlock-detection-recovery/)
- [Deadlock, Starvation, and Livelock](https://www.geeksforgeeks.org/deadlock-starvation-and-livelock/)
- [Deadlock Prevention And Avoidance](https://www.geeksforgeeks.org/deadlock-prevention/)

