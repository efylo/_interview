# Critical Section

## Abstract

Critical section refers the code segment where there exist shared variables or resources among different processes or threads. 

---

## Example

For example, if you want to count 100,000 for each thread in a global variable, then it might not work properly since addition need two steps. Load from a global variable, add 1 and store. If *load* happens in a thread before *store* happens in another thread then counting a number among multiple threads fail. 

Though, this not really happens when small number of instructions per thread is done. 

### Example pseudo code (assembly)

```pseudocode
"""
Assumption
1) x10 is temporary register
2) x9 is a register that stores address of global count value
"""
Process
Thread 1: Load x10, 0(x9)
"""Thread 1 => 2"""
Thread 2: Load x10, 0(x9)
Thread 2: Add x10, x10, 1
Thread 2: Store 0(x9), x10
"""Thread 2 => 1"""
Thread 1: Add x10, x10, 1
Thread 1: Store 0(x9), x10
"""
Initially wanted 0(x9) to be added twice, 
though 0(x9) added once due to critical section problem
"""
```

### Implementation in Python

In Python, there exists built-in library that can solve critical section problems. In Python [threading](https://docs.python.org/ko/3/library/threading.html) module, use of *Thread* and *Lock* class can solve the critical section problem. 

Different part of using *Lock* object is that the thread is **blocked** when it cannot acquire *Lock* object. Besides using *Lock*, there exist many other synchronization classes like *Semaphore*, *Event*, *Barrier*, etc. 

*Lock* is an object (or instance) in python, so it doesn't have to be globalized. Using *Lock* as an input may be a good way in implementation. 

```python
from threading import Thread, Lock

def f(key: Lock):
    global x
    # critical section running million times
    for _ in range(1000000):
        # return True if acquired, else block
        if key.acquire():   
            x += 1          # critical section
            key.release()   # release Lock
            
def main():
    global x
    x = 0
    key = Lock()            # Lock object
    thread1 = Thread(target=f, args=(key, ))
    thread2 = Thread(target=f, args=(key, ))
    print(x)

if __name__ == "__main__":
    main()
```

---

## Code

- [ex_lock.py](./codes/ex_lock.py)

---

## Reference

- [Critical Section in Synchronization](https://www.geeksforgeeks.org/g-fact-70/)
- [threading — 스레드 기반 병렬 처리 — Python 3.10.0 문서](https://docs.python.org/ko/3/library/threading.html)

