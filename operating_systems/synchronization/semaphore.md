# Semaphore

## Abstract

Semaphore was proposed by Dijkstra in 1965. Used to synchronize multiple processes or threads using a single integer value. There are two types of semaphore

---

## Types

1. Binary Semaphore

   a.k.a Mutex Lock, e.g) python *Lock* in *threading* library

2. Counting Semaphore

   Access is controlled via the number of the counting semaphore

---

## Functions

```python
from threading import Thread


class Semaphore_:
    """simple semaphore class"""
    def __init__(self, value) -> None:
        self.s = value
        pass

    def P(self, i: int):
        while self.s == 0:
            print(f'An instance is running - from id {i}')
            pass
        self.s -= 1
    
    def V(self, ):
        self.s += 1


def f(s: Semaphore_, i: int):
    """thread to run"""
    # ask for semaphore acquire
    s.P(i)
    # do some functionality - if costly, then it is blocked from other thread sometimes
    x = [1, 2, 3, 4]
    for i in range(100):
        for j in range(100):
            x[(100*i+j)%4] += 1 if j%2 == 0 else -1
    # increase s
    s.V()
    

def main():
    sema = Semaphore_(1)
    threads = []
    for i in range(10000):
        threads.append(Thread(target=f, args=(sema, i, )))
    
    for i in range(10000):
        threads[i].start()


if __name__ == "__main__":
    main()
```

### Processes possible

Let me assume 2 threads, *thread1* and *thread2*. 

There mainly exist 6 atomic instructions. P(s), CS, V(s) for each thread. Let me denote them P~1~, CS~1~, V~1~ for *thread1*. 

Also, let *thread1* as initial thread operating P1. This is possible since we can interpret *thread2* as *thread1* if *thread2* is initial. 

1. **P~1~-CS~1~-V~1~-P~2~-CS~2~-V~2~**

   Execution as if *thread1* and *thread2* are both atomic. 

2. **P~1~-P~2~-CS~1~(-P~2~)-V~1~-CS~2~-V~2~**

   1-1. **(P~1~-P~2~)**: P~2~ is blocked since semaphore is 0, due to P~1~

   1-2. **(P~1~-P~2~-CS~1~)**: Critical section of *thread1* held

   1-3. **(P~1~-P~2~-CS~1~-V~1~)**: Semaphore unblocked, return *thread1*

   1-4. **(..-CS~2~-V~2~)**: return *thread2*

   Since *thread2* is blocked in 1-1, cannot execute CS~2~, V~2~ in 1-2, 1-3, 1-4. 

   P~2~ is always blocked if executed before V~1~

---

## Difference between Binary and Counting

Initial Semaphore s is 1 in Binary Semaphore. Though, in Counting Semaphore initial value of s is n, which is the number of processes (or threads) you want to execute inside critical section. If s is initially 3, then maximum 3 processes (or threads) could enter into the critical section. It is like waiting for a roller coaster in amusement park. Only limited number of people could get into the roller coaster. 

---

## Limitations

- **Priority Inversion**

  Higher priority process has to wait until lower priority process is finished

- **Deadlock**

  When a process wakes up other process in execution. Then semaphore s is not incremented, causing deadlock. 

- **Busy wait**

  Way of blocking a process is to loop until semaphore is available. 

  Maybe, busy wait is occurred due to the concept of symmetric multiprocessing. Since process not in execution cannot be signaled by other processes. 

---

## Mutex vs. Semaphore

The key difference in mutex and semaphore is that mutex is locking mechanism, rather semaphore is signaling mechanism. Though using semaphore in binary way, it seems quite similar. 

I think the word *signaling* refers the process or thread calls *V* to signal others that now the execution is available. Though *locking* may refer to the fact that the process executed is the subject in lock and unlock. The load of listening is on other processes when using locks. These are my wonders about the difference of mutex in locking mechanism and semaphore in signaling mechanism. 

What I think is when I have to deal with the program using global variable or input as a pointer, then *Mutex* is better. But for the program that multiple threads operate on local variables but cost heavy, then *Semaphore* is better. 

---

## Reference

- [Semaphores in operating system](https://www.geeksforgeeks.org/semaphores-operating-system/)
- [Mutex vs Semaphore](https://www.geeksforgeeks.org/mutex-vs-semaphore/)