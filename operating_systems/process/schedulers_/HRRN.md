# Highest Response Ratio Next (HRRN)

## Abstract

Highest Response Ratio Next is the scheduling algorithm which selects the next process to run via the response ratio. Looking through the below function, I interpreted that the response ratio is a function of waiting time and burst time that ages naturally. As the process waits for longer time, gradually the response ratio will grow, then will be selected by the scheduler. Also, this scheduling algorithm is non-preemptive. 

```pseudocode
Response ratio = (Wait_time + Burst_time) / Burst_time
```

Since waiting time is initially zero, the response ratio is initially 1. Gro

---

## Reference

- [Highest Response Ratio Next (HRRN) Scheduling](https://www.geeksforgeeks.org/operating-system-highest-response-ratio-next-hrrn-scheduling/)
