from collections import deque
from queue import Queue


# Queue class - O(1) operations, circular Queue <-> limited in size
class Queue_:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.front = 0          # front
        self.rear = maxsize - 1 # rear
        self.qsize = 0          # num. of items
        self.queue = [None]*maxsize
    
    def empty(self):
        return self.qsize == 0
    
    def full(self):
        return self.qsize == self.maxsize
    
    def enqueue(self, item):
        if self.full():
            return
        self.rear = (self.rear+1) % self.maxsize
        self.queue[self.rear] = item
        self.qsize += 1
    
    def dequeue(self):
        if self.empty():
            return
        ret = self.queue[self.front]
        self.queue[self.front] = None
        self.front += 1
        self.qsize -= 1
        return ret
    
    def getFront(self):
        if self.empty():
            return
        return self.queue[self.front]
    
    def getRear(self):
        if self.empty():
            return
        return self.queue[self.rear]
    
    def __repr__(self):
        return f'queue={self.queue}, front={self.front}, rear={self.rear}, qsize={self.qsize}'


def QueueList():
    queue = []
    print(f'----Queue(list) created----')

    # enqueue
    queue.append('a')
    queue.append('b')
    queue.append('c')
    print(f'queue as a list: {queue}')    # ['a', 'b', 'c']

    
    f = queue[0]    # 'a'
    print(f'front: {f}', end=', ')
    r = queue[-1]   # 'c'
    print(f'rear: {r}')

    print('removed: ', end="")
    # dequeue
    print(f'{queue.pop(0)}', end=', ')    # 'a'
    print(f'{queue.pop(0)}', end=', ')    # 'b'
    print(f'{queue.pop(0)}', end='\n')    # 'c'

    return


def QueueDeque():
    queue = deque([], 5)
    print(f'\n----Queue(deque) created----')

    # enqueue
    queue.append('d')
    queue.append('e')
    queue.append('f')
    print(f'queue as a deque: {queue}')

    f = queue[0]    # 'd'
    print(f'front: {f}', end=', ')
    r = queue[-1]   # 'f'
    print(f'rear: {r}')

    print('removed: ', end="")
    # dequeue
    print(f'{queue.popleft()}', end=', ') # 'd'
    print(f'{queue.popleft()}', end=', ') # 'e'
    print(f'{queue.popleft()}', end='\n') # 'f'

    return


def QueueQueue():
    queue = Queue(5)
    print(f'\n----Queue created----')

    # enqueue
    queue.put_nowait('g')
    queue.put_nowait('h')
    queue.put_nowait('i')
    print(f'maxsize: {queue.maxsize}, qsize: {queue.qsize()}')

    # dequeue
    print(f'{queue.get_nowait()} removed, qsize: {queue.qsize()}')
    print(f'{queue.get_nowait()} removed, qsize: {queue.qsize()}')
    print(f'{queue.get_nowait()} removed, qsize: {queue.qsize()}')

    return


def main():
    QueueList()
    QueueDeque()
    QueueQueue()


if __name__ == "__main__":
    main()
