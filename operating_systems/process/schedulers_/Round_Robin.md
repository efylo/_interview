# Round Robin

## Abstract

In round robin scheduling algorithm, all processes in ready-queue fairly gets the chance to use the CPU. So it ensures no starvation among processes. It is preemptive, and one of the most commonly used technique in CPU scheduling. Though, there exist overloads in context switching. Running a program that requires lots of CPU usage might be too slow in round robin scheduler. 

Term *quantum time* is used in round robin scheduling algorithm. The quantum time is the number of unit time that each process is allowed to use. Quantum time 3 means that each process is executed in CPU for 3 times unit time. So, I think the only possible change this algorithm can make is through use of different quantum times. 

---

## Selfish

A selfish round robin algorithm, is an algorithm devised by adding one more variable. A variable is if the processes is new to this queue or not. 

### NEW Queue

- When the process enters the ready queue, except when the process is the first one to arrive
- The priority grows till 'a', which is bigger than the upper limit of accepted queue. 

### ACCEPTED Queue

- After the CPU has accepted, the process then goes to accepted queue. 
- The priority grows till 'b', which is smaller than 'a'.
- Since the maximum priority possible is smaller than that of new queue, in some time the process of new queue is executed. 

By manipulating the difference between 'a' and 'b', I think it's possible to change how selfish this algorithm is. 

---

## Reference

- [Program for Round Robin scheduling](https://www.geeksforgeeks.org/program-round-robin-scheduling-set-1/)
- [Round Robin Scheduling with different arrival times](https://www.geeksforgeeks.org/round-robin-scheduling-with-different-arrival-times/)
- [Selfish Round Robin Scheduling](https://www.geeksforgeeks.org/selfish-round-robin-cpu-scheduling/)