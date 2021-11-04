# Stack

A linear data structure which insertion and deletion happens at same end(top). Only at the top where push and pop operation can happen. It follows LIFO(Last In First Out) order. 

## Abstract

- a linear data structure
- follows order in the operations(*LIFO*; last in first out, *FILO*; first in last out)
- *push*: adds an item to the top of the stack, raises overflow when stack is full
- *pop*: removes an item on top of the stack, raises underflow when stack is empty
- *peek* or *top*: returns an item on top of the stack, 
- *isEmpty*: true if stack is empty, false if not
- time complexities: all functions take constant time, O(1)

---

## in Python (implementation)

### list

- append() = push(), pop() = pop()
- push and pop operation's time complexity is not constant, depends on the size
- thus, not preferred for implementing stack

### collections.deque

- append() = push(), pop() = pop()
- O(1) for push and pop
- maxlen - maximum number of items possible
- thus, preferred for stack
- also supports appendleft(), popleft()
- access to each element is slower than list

### queue.LifoQueue

- support functionalities for multi-threads
  - such as *block*, *timeout*, *put()*, *get()*, 
- not subscriptable - use [idx] to index the element
- not printable - elements are not displayable
- put_nowait() = push(), get_nowait() = pop()
  - *nowait* for not waiting for stack is not full when put(), not empty when get()
- maxsize - maximum number of items possible in queue
- put(), get() - wait until an item is available
- empty(), full() - check if queue is empty or full(maxsize)
- qsize() - return the number of items, if full return QueueFull

---

## Applications

- symbol balancing ("", '', {}, [], (), ...)
- infix to postfix/prefix (a+b => ab+, +ab, ...)
- redo-undo, forward-backward features
- backtracking - coming back to the previous state, choose another path
- graph algorithms
- memory management - modern computer uses a stack
- string reversal

---

## Codes

- [stack.py](./codes/stack.py)

---

## Reference

- [Stack Data Structure](https://www.geeksforgeeks.org/stack-data-structure/#intro)
- [Stack Data Structure (Introduction and Program)](https://www.geeksforgeeks.org/stack-data-structure-introduction-program/)
- [Stack in Python](https://www.geeksforgeeks.org/stack-in-python/)
- [collections — 컨테이너 데이터형 — Python 3.10.0 문서](https://docs.python.org/ko/3/library/collections.html)
- [queue — 동기화된 큐 클래스 — Python 3.7.12 문서](https://docs.python.org/ko/3.7/library/queue.html)

