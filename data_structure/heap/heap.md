# Heap

## Abstract

a binary tree which follows some constraints. 

constraints are, 

1. heap is a complete tree, (completely filled)
2. either min or max heap, parent node lesser or greater than child nodes

---

## Applications

- Priority Queue

- Heap Sort - O(n logn)

  Build a heap - replace index 0 with last one - Build a heap with size-1 - replace - ... until a heap size is 1

  if min heap, then an array is in decreasing order, else in increasing order. 

- Dijkstra's Shortest Path with Adjacency List, and so on

---

## Codes

- [heap.py](./codes/heap.py)

---

## Reference

- [Heap Data Structure](https://www.geeksforgeeks.org/heap-data-structure/)
- [Binary Heap](https://www.geeksforgeeks.org/binary-heap/)
- [Heap Sort](https://www.geeksforgeeks.org/heap-sort/)