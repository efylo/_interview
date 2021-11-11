# Multilevel Queue(MLQ)

## Abstract

Processes can have their own characteristics. There are foreground (interactive) processes, background (batch) processes, and many others. Multilevel Queue is to give different level of priority via the characteristic of the processes. For example, a queue of system processes gets the highest priority, then of interactive processes gets next, and so on. 

---

## Scheduling

Scheduling in multilevel queue is possible in two ways. 

One is the scheduling algorithm for each queue. 

- Each queue can run on different scheduling algorithms. 
- e.g) System processes run on round robin, interactive processes run on FCFS, etc.

Another is the scheduling algorithm among the queues. 

- **Fixed priority preemptive scheduling method**

  Each queue has its own priority, and one with higher priority firstly gets to use the CPU. 

  The problem is, the starvation for low-priority queue. Since the jobs in high priority queue are firstly selected, there may be no chance for jobs in low priority queue to use the CPU. 

- **Time slicing**

  The solution for the first method is to slice the time for each queue. High priority queue will probably receive more CPU time to use, and low priority queue will receive less than higher ones. 

  Through this method, even jobs in lowest priority queue can use the CPU for the given time-slice. Though, they will be able to use the CPU smaller time than of jobs in higher ones. 

---

## Pros & Cons

### Pros

- Processes are permanently assigned to the queue, low overhead exists

### Cons

- Processes in low priority queues may starve
- Inflexible in nature - can possibly solve through **MultiLevel Feedback Queue**

---

## Multilevel Feedback Queue(MLFQ)

Given the concept of multilevel queue, MLFQ has difference that processes of each queue can move from queue to queue. The movement of queues is decided through analyzing the behavior of process. 

Generally, high-priority queue runs the processes in round-robin algorithm for specific time quantum. Smaller time quantum goes to higher priority queue. When process first enters the queue, it goes to the queue of highest priority. Then if the process not finishes in the given time quantum, the priority level flows down to the queue of below-level. 

MLFQ is pre-emptive scheduling algorithm, so arrival of the process of higher priority can preempt currently running process. 

### Problem & Solution

- Processes of low-level queues might not get chance to run on the CPU
- Through boosting low-priority processes to the highest priority queue after some interval, starvation problem could be solved

### Reasons in use

- More flexible than multilevel queue
- Can optimize turnaround time even though there are no information about running time of the process
- Reduce in response time

### Pros

- flexible, allow different processes to move between queues
- prevent starvation by boosting the priority

### Cons

- produce more CPU overheads
- the most complex algorithm

---

## Reference

- [Multilevel Queue Scheduling](https://www.geeksforgeeks.org/operating-system-multilevel-queue-scheduling/)
- [Multilevel Feedback Queue Scheduling](https://www.geeksforgeeks.org/multilevel-feedback-queue-scheduling/)