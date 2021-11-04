# Priority Queue

## Abstract

- an extended version of queue
- every item has a priority(우선순위)
- higher priority item is dequeued before one with lower priority
- if priority is same, follows the order of the queue(FIFO)

---

## Operations

- insert(item, priority): inserts an item with given priority
- getHighestPriority(): returns the highest priority item
- deleteHighestPriority(): removes the highest priority item
  - these can all derive from MinHeap
  - though, heap must use priority in comparison

---

## Binary Heap

- most common way to implement priority queue
- a complete binary tree
- min, max heap - parent smaller / bigger than child nodes always
- level order traversal

### adjacent node to i'th node

| index       | description          |
| ----------- | -------------------- |
| A[(i-1)//2] | the parent node      |
| A[(2*i)+1]  | the left child node  |
| A[(2*i)+2]  | the right child node |

### methods (min heap)

- push(item) - pushes an item to the heap
- extractMin() - returns and removes minimum of heap
- getMin() - returns minimum item of heap
- decreaseKey(i, val) - decrease heap[i] to val
- deleteKey(i) - delete heap[i]
- to implement above methods, need *heapify*, *heappop*, *heappush*

---

## Code

- [minheap.py](./codes/minheap.py)

---

## Reference

- [Priority Queue | Set 1 (Introduction)](https://www.geeksforgeeks.org/priority-queue-set-1-introduction/)
- [Binary Heap](https://www.geeksforgeeks.org/binary-heap/)