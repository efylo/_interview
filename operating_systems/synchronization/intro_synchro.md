# Intro to Process Synchronization

## Abstract

There exist two processes, which are

- Independent Process

  Executing independent process doesn't affect other processes

- Cooperative Process

  Executing cooperative process affects other processes

Thus, process synchronization is needed only for cooperative processes. 

---

## Race Condition

The condition when multiple processes execute the same code, access the same memory, or use of shared variables. This then leads to race condition, which results in wrong value. Also, it refers to multiple threads accessing a critical section. Use of locks or make the instructions of a critical section an atomic value can prevent race condition. 

---

## Critical Section Problem

Critical section is a section of a program where only one process has to access. There could be critical section and remainder section inside a program. 

### Requirements for the Solution

- Mutual Exclusion

  When a process has entered the critical section, no other processes can enter

- Progress

  Only the processes which are not executing remainder section is allowed to use the critical section. 

- Bounded Waiting

  The number of processes waiting for the entrance of critical section needs to be bounded. 

---

## Peterson's Solution

### Global Variables

- boolean flag[i]
- int turn

### Example code (not process, but thread)

```python
from threading import Thread

def peterson(i: int, flag: list):
    # flag can be entered by a pointer
    global turn
    while True:
        flag[i] = True;
        j = (i+1)%2
        turn = j
        while flag[j] and turn==j:
            critical_section()
            flag[i] = False
            remainder_section()

# thread creation by Thread module
thread = Thread(target=peterson, args=(i, flag))
```

### Description

Critical section is executed only when i'th process(or thread) wants to, and it's i'th process's turn to do the critical section. Whenever other process or thread makes global variable turn to their number, then i'th process will be expelled from the section. Also, the process cannot execute critical section until they finish their remainder section. 

But, Peterson's solution makes busy waiting. Since the process is not idle in waiting, they have to knock until they can get to execute the critical section. Also, more than 2 processes or threads is not possible. Since you have to hand over global variable *turn*, but it's not quite possible if you use more than 2 processors. Given 2 processors, handing over turn to another process is always correct, but is not if more than 2 processors co-exist. 

---

## TestAndSet (Lock)

### Global Variable

```pseudocode
if critical_section == unlocked, then lock = 0
else then lock = 1
```

### Steps

0. Before entering, a process asks if locked.
1. If locked, then wait until unlock(freed)
2. If process gets the lock, executes the critical section

### Pseudo-code

```python
def test_and_set():
    global lock
    while True:
        if lock == 0:
            enter_CS()

def enter_CS():
    global lock
    lock = 1
    leave_CS()

def leave_CS():
    global lock
    lock = 0
```

### Description

Mutual exclusion and progress is guaranteed, but bounded waiting is not since there could be multiple waiting processes. The difference between Peterson's solution is that using the lock is more active, since previous solution has to wait until another process gives the turn. 

---

## Codes

- [peterson.py](./codes/peterson.py)

  Code of Peterson algorithm through python threading module. Code flows too slow sometimes, too fast other times that the concept of threading is not applied. May due to busy waiting, the process is too slow. 

- [testandset.py](./codes/test_and_set.py)

  Using the concept of lock, ensures no dead lock happens. It also guarantees mutual exclusion and progress. Also, it is much faster than Peterson's solution. 

---

## Reference

- [Process Synchronization | Introduction](https://www.geeksforgeeks.org/process-synchronization-set-1/)
- [피터슨의 알고리즘 - 위키백과, 우리 모두의 백과사전](https://ko.wikipedia.org/wiki/피터슨의_알고리즘)
- [threading — 스레드 기반 병렬 처리 — Python 3.10.0 문서](https://docs.python.org/ko/3/library/threading.html)

