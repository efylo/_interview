# Process Schedulers in OS

## Abstract

*Why is it essential to schedule the processes?* 

It's because multiprogramming in operating systems is one of the essential part nowadays. Those operating systems mostly use time multiplexing, executing processes for a certain time which is called quantum. 

---

## Types

1. **Long term** - Job scheduler

   Job scheduler cares about the processes in the ready state, and the number of processes in them is called degree of multiprogramming. Since a process in the ready state can immediately executed since they are generally on the main memory. 

   Also, it is important to specify tasks which takes more time in I/O operations (IO bound process) and in CPU operations (CPU bound process). I/O operations and CPU operations can simultaneously operated, so it is crucial to fully use I/O devices and CPU simultaneously to increase the efficiency of a computer. 

2. **Short term** - CPU scheduler

   The scheduling algorithms like round robin, first come first served are basically part of the CPU scheduler. Choosing a process to run from processes of ready state is what CPU scheduler is responsible for. Typical concern is to not make any process that starve. 

   Dispatcher is what really do the context switching between running process and selected process by CPU scheduler. It switches the context, switches to user mode, and jump to the proper location of currently loaded program. 

3. **Medium term**

   If I run my laptop for a long time, there are processes that resides on one of the windows but not really in the ready state. If the process is in the ready state, then switching the window to that process must be smooth enough that no re-creation occurs. Though, some of the processes are newly created if I move currently running window to some long-time neglected process. I think these some long-time neglected ones might be in the suspended ready or wait state. 

   Using a smart medium-term scheduler will probably make the computer faster, since running more processes at the ready state will probably slow down your computer due to smaller memory allotment to each process. 

---

## Terms in Time

1. **Arrival time**: Time when the process arrives at the ready queue
2. **Completion time**: Time when the process completed
3. **Burst time**: Time required by a process for CPU execution(running time)
4. **Turnaround time**: Completion time - Arrival time, Time from arrival to completion
5. **Waiting time**: Turnaround time - burst time, time inside the ready queue

---

## Objectives

1. **Maximize CPU utilization** (minimize idle)
2. **Fair allocation of CPU** (less starvation)
3. **Matimize throughput** (the number of completed processes per time unit)
4. **Minimize turnaround time**
5. **Minimize waiting time**
6. **Minimize response time**

---

## Scheduling Algorithms (Quite many)

1. First Come First Serve (FCFS)
2. Shortest Job First (SJF)
3. Longest Job First (LJF)
4. Shortest Remaining Time First (SRTF)
5. Longest Remaining Time First (LRTF)
6. Round Robin Scheduling
7. Priority Based scheduling (Non-preemptive)
8. Highest Response Ratio Next (HRRN)
9. Multilevel Queue Scheduling
10. Multi level Feedback Queue Scheduling

---

## Facts

- FCFS suffers from convoy effect (long waiting times possible)
- SJF, SRTF cause starvation (long processes never get to use CPU)
- Round Robin with time quantum large, acts same as FCFS
- SJF minimizes average waiting time, though there doesn't exist possible way of predicting how long the job will take. 

---

## References

- [Process Schedulers in Operating System](https://www.geeksforgeeks.org/process-schedulers-in-operating-system/)
- [CPU scheduling in Operating Systems](https://www.geeksforgeeks.org/cpu-scheduling-in-operating-systems/)