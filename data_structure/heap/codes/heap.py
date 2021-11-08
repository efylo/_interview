from heapq import heappush, heappop, heapify
from typing import Iterable
from collections import deque


# internal method
# __swap(a, b) = swap heap[a] and heap[b]
# __pathFind() = return a list of path till last index
# __heapify(idx) = heapify heap[idx], assume the children of heap[idx] are heap, and heap[idx] is not heap
# __heappop() = pop heap[0], make popped heap fits the condition

# external method
# getMin() = return heap[0]
# extractMin() = return and remove heap[0]
# decreaseKey(key, x) = decrease a key to x, make heap
# insert(x) = insert new element x into heap
# delete(x) = delete element x
class MinHeap:
    def __init__(self) -> None:
        self.heap = []
    
    def getMin(self, ):
        return self.heap[0]
    
    def __swap(self, a, b):
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp
    
    # pathFind()
    # returns a path from index 0 to the last index
    def __pathFind(self, ):
        ret = deque()
        # the last index
        idx, n = 0, len(self.heap)-1
        if idx == n:
            return ret
        while n != idx:
            ret.appendleft(n)
            n = (n-1)//2
        return ret
    
    # heapify(idx)
    # assume children of idx are both heaps(can be only child or none)
    # if heap[idx] is not minimum, swap with min(heap[left], heap[right])
    # then recursively heapify(min_idx(left, right))
    def __heapify(self, idx):
        # no child
        if 2*idx+1 >= len(self.heap):
            return
        # only child
        if 2*idx+2 == len(self.heap):
            if self.heap[idx] > self.heap[2*idx+1]:
                self.__swap(idx, 2*idx+1)
                return
            return
        # both children
        min_idx = min(idx, 2*idx+1, 2*idx+2, key=lambda x: self.heap[x])
        if min_idx == 2*idx+1:
            self.__swap(idx, 2*idx+1)
            return self.__heapify(2*idx+1)
        if min_idx == 2*idx+2:
            self.__swap(idx, 2*idx+2)
            return self.__heapify(2*idx+2)
        return

    # heappop
    # __pathfind = a list of indexes to the last index of heap
    # __swap(idx, next_idx) until the last index
    # after swap, if another child of idx is smaller than idx,
    # then __swap(idx, another child) and __heapify(another child)
    def __heappop(self, ):
        idx = 0
        path = self.__pathFind()
        for p in path:
            self.__swap(idx, p)
            if p == 2*idx+1:
                if p == path[-1]:
                    break
                if self.heap[idx] > self.heap[2*idx+2]:
                    self.__swap(idx, 2*idx+2)
                    self.__heapify(2*idx+2)
            if p == 2*idx+2:
                if self.heap[idx] > self.heap[2*idx+1]:
                    self.__swap(idx, 2*idx+1)
                    self.__heapify(2*idx+1)
                
            idx = p
        return self.heap.pop()

    def popMin(self, ):
        return self.__heappop()
    
    # fails if no key in heap
    def decreaseKey(self, key, x):
        idx = self.heap.index(key)
        if self.heap[idx] > x:
            self.heap[idx] = x
            while idx > 0:
                parent = (idx-1) // 2
                if self.heap[parent] < self.heap[idx]:
                    break
                self.__swap(parent, idx)
                idx = parent
    
    def insert(self, x):
        # heappush(self.heap, x)
        idx = len(self.heap)
        self.heap.append(x)
        while idx > 0:
            parent = (idx-1) // 2
            if self.heap[parent] < self.heap[idx]:
                break
            self.__swap(parent, idx)
            idx = parent
                    
    def delete(self, x):
        self.decreaseKey(x, float("-inf"))
        self.extractMin()
    
    def __repr__(self) -> str:
        return f'MinHeap {self.heap}'


def printHeap(x: Iterable):
    i = 0
    n = len(x)
    while True:
        i2 = (i+1)*2 - 1
        print(x[i:min(n, i2)])
        if n <= i2:
            break
        i = i2


x = MinHeap()
x.insert(1)
x.insert(3)
x.insert(5)
x.insert(2)
x.insert(4)
x.insert(6)
x.insert(0)

print(x.extractMin())
print(x)