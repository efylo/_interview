# SJF / SRTF

## Abstract

From the word 'shortest job first', it's a scheduling algorithm that makes the shortest job as the next process to run(non-preemptive). Due to the reason that short jobs always run on the CPU, it can cause starvation of long jobs, though it can be solved through the concept of aging. Some paradox to this algorithm is that we do not know precisely how the job will end. But in some environments that running time of the job is known, this may be optimal in reducing average waiting time. 

A preemptive version of SJF is know as SRTF which stands for shortest remaining time first. If a job comes to ready state with shorter remaining time than the currently running job, then SRTF scheduler makes context switching. 

---

## Implementation

We just need to sort the processes with minimum arrival time, and minimum burst time. 

The difference in implementation between SJF and SRTF is when the process arrives to the ready queue. For SRTF scheduler, the remaining time of currently arrived process is immediately compared to the remaining time of currently running process. 

---

## Prediction

As we do not exactly know how long will the process take, there exists some prediction techniques. 

1. Static method

   Predicting the burst-time by process size and type

2. Dynamic method

   Given the information of the actual burst-time of the process, prediction is held by averaging prior burst-times. 

   - Simple average - E[P]
   - Exponential average(Aging) - multiply weights to previous processes, which makes the previous burst time smaller. 

---

## Reference

- [Program for Shortest Job First (or SJF) CPU Scheduling | Set 1 (Non- preemptive)](https://www.geeksforgeeks.org/program-for-shortest-job-first-or-sjf-cpu-scheduling-set-1-non-preemptive/)
- [Program for Shortest Job First (SJF) scheduling | Set 2 (Preemptive)](https://www.geeksforgeeks.org/program-for-shortest-job-first-sjf-scheduling-set-2-preemptive/)
- [Shortest Job First CPU Scheduling with predicted burst time](https://www.geeksforgeeks.org/shortest-job-first-cpu-scheduling-with-predicted-burst-time/)

