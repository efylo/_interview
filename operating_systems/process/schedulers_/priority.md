# Priority

## Abstract

Generally used in batch systems, the word 'priority' means that each process gets a priority of its own. Process of the highest priority gets to use the CPU, and if the priority is same then executed in first come first serve mechanism. 

Priority is decided upon memory, time or any other resource requirements. 

The main problems are indefinite blocking or starvation for the process of low-priorities. The aging method that the priority of low-priority queues gradually increases is used to solve the problem. 

---

## Implementation

In implementing priority queue, Min Heap is generally used. Below are the main functions used in implementing priority scheduling. 

The Components are, 

- structure of process [pid, burst-time, response-time, priority, arrival-time]
- a list of processes
- a heap for building priority queue
- functions to sort an array
- functions to insert and extract the process from the heap
- functions to manage scheduling
- and so on

---

## Reference

- [Priority Scheduling](https://www.geeksforgeeks.org/program-priority-scheduling-set-1/)
- [Program for Preemptive Priority CPU Scheduling](https://www.geeksforgeeks.org/program-for-preemptive-priority-cpu-scheduling/)
- [Priority Scheduling with different arrival time – Set 2](https://www.geeksforgeeks.org/operating-system-priority-scheduling-different-arrival-time-set-2/)

