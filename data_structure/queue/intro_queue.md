# Queue

## Abstract

- a linear structure
- follows a particular order in the operations(FIFO; first in first out)
- *enqueue*: adds an item to rear of the queue, raises overflow if queue full
- *dequeue*: removes an item from front of the queue, raises underflow if queue empty
- *front*: get the front item from queue
- *rear*: get the last item from queue
- time complexity: all functions take constant time, O(1)

---

## Caution

- *dequeue* makes *front* incremented by 1, which then makes size of queue smaller
- solution is to increment both *front* and *rear* in *dequeue*
- the solution makes queue to have *circular* characteristic

---

## in Python (Implementation)

### list

- append() = enqueue(), pop(0) = dequeue()
- front = List[0], rear = List[-1]
- not preferred, since enqueue and dequeue are not O(1)
- creation of class Queue possible, though using pre-defined module is recommended

### collections.deque

- append() = enqueue(), popleft() = dequeue()
- front = Deque[0], rear = Deque[-1]
- preferred over list, O(1) for all 4 operations
- also supports maxlen, maximum possible size of queue

### queue.Queue

- put_nowait() = enqueue(), get_nowait() = dequeue()
- can't actually access front and rear elements
- supports complex functionalities for multi-threads
  - *put()*, *get()*, *block*, *timeout*

---

## Applications

- for things don't need immediate procedure
- a resource sharing between multiple consumers (CPU, Disk Scheduling)
- asynchronous transfer of data (IO Buffers, pipes, file IO, ...)

---

## Codes

- [queueue.py](./codes/queueue.py)

---

## Reference

- [Queue Data Structure](https://www.geeksforgeeks.org/queue-data-structure/)
- [Queue | Set 1 (Introduction and Array Implementation)](https://www.geeksforgeeks.org/queue-set-1introduction-and-array-implementation/)
- [Queue in Python](https://www.geeksforgeeks.org/queue-in-python/)