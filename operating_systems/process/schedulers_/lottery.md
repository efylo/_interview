# Lottery Process Scheduling

## Abstract

Lottery scheduling is random-selection based scheduling algorithm. It could be implemented in both preemptive and non-preemptive way. Since each process gets at least one lottery tickets, there is no possibility of starvation. 

For a time slice, the winning ticket is picked and the process gets to use the CPU. The winning probability of the process having more tickets is higher than the process with lower number of tickets. 

---

## Manipulation of tickets

### Ticket Currency

Tickets are given to different users, and the user can give the tickets to their own processes. User with more processes, then each process will possess lower probability of winning. 

### Transfer Tickets

A process can transfer its tickets to other process

### Ticket Inflation

A process can temporarily raise, lower the number of tickets of its own

---

## Reference

- [Lottery Process Scheduling](https://www.geeksforgeeks.org/operating-system-lottery-scheduling/)