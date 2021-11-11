# Starvation and Aging

## Abstract

The priority scheduling seems quite fancy, though it suffers from the critical problem called starvation. Starvation of the process can be understood that the process is starving for the CPU. So that some of the processes are indefinitely waiting for themselves to be executed. 

Deadlock is also the problem that the process can't be executed. But the reason is different. Starvation happens because of the logical faults in the architecture, though deadlock happens by the process indefinitely occupying resources. For example, infinite loop in the program makes the process not proceed further, which could be considered as a deadlock. 

---

## Solution - Aging

As a solution, the priority of a process ages as the waiting time passes. 

---

## Reference

- [Starvation and Aging in Operating Systems](https://www.geeksforgeeks.org/starvation-and-aging-in-operating-systems/)