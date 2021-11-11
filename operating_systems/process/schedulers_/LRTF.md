# Longest Remaining Time First(LRTF)

## Abstract

LRTF, according to the name, is an algorithm to make running process which has the longest remaining time. Though, it is not easy to explicitly understand why this algorithm or scheduler is used. By looking through the examples, I could barely understand why this scheduler is used. 

Looking through the example below, the processes run in quite a fair manner for a long time. If the unit time(quantum) is quite small, then the process will look like as if they are running in a simultaneous manner. 

The scheduler will execute the process of longest remaining time until the remaining times of all processes become same. After this portion, processes will run like round-robin. 

---

## Example

[Arrival-time, Burst-time] in ms

P1 = [0, 2] / P2 = [1, 4] / P3 = [2, 6] / P4 = [3, 8]

Executed process of the time is marked **bold**

| time \ remaining time | P1    | P2    | P3    | P4    |
| --------------------- | ----- | ----- | ----- | ----- |
| 1                     | **1** | -     | -     | -     |
| 2                     | 1     | **3** | -     | -     |
| 3                     | 1     | 3     | **5** | -     |
| 4                     | 1     | 3     | 5     | **7** |
| 5                     | 1     | 3     | 5     | **6** |
| 6                     | 1     | 3     | **5** | 5     |
| 7                     | 1     | 3     | 4     | **5** |
| 8                     | 1     | 3     | **4** | 4     |
| 9                     | 1     | 3     | 3     | **4** |
| 10                    | 1     | **3** | 3     | 3     |
| 11                    | 1     | 2     | **3** | 3     |
| 12                    | 1     | 2     | 2     | **3** |
| 13                    | 1     | **2** | 2     | 2     |
| 14                    | 1     | 1     | **2** | 2     |
| 15                    | 1     | 1     | 1     | **2** |
| 16                    | **1** | 1     | 1     | 1     |
| 17                    | 0     | **1** | 1     | 1     |
| 18                    | 0     | 0     | **1** | 1     |
| 19                    | 0     | 0     | 0     | **1** |
| 20                    | 0     | 0     | 0     | 0     |

---

## Reference

- [Longest Remaining Time First (LRTF) CPU Scheduling Algorithm](https://www.geeksforgeeks.org/longest-remaining-time-first-lrtf-cpu-scheduling-algorithm/)
- [Longest Remaining Time First (LRTF) CPU Scheduling Program](https://www.geeksforgeeks.org/longest-remaining-time-first-lrtf-cpu-scheduling-program/)

