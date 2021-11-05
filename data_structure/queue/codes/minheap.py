# almost self-made minimum heap
# push, pop, heapify method on my own (using heapq module - heapify, heappush, heappop recommended)
# other methods copyright of codes on https://www.geeksforgeeks.org/binary-heap/
class MinHeap:
    def __init__(self) -> None:
        self.items = []

    def __swap(self, a, b):
        temp = self.items[a]
        self.items[a] = self.items[b]
        self.items[b] = temp
    
    # heap push algorithm - using heappush in heapq module recommended
    def push(self, item):
        self.__push(item)
    
    # recursive push, external access limited
    def __push(self, item, i=0):
        l = len(self.items)
        if i == l:
            self.items.append(item)
            return
        # choose left/right
        while l != 2*i+1 and l != 2*i+2:
            l = (l-1)//2
        # no change
        if self.items[i] <= item:
            self.__push(item, l)
            return
        # change item
        old_item = self.items[i]
        self.items[i] = item
        self.__push(old_item, l)
        return

    # must assume both children are heapified
    def __heapify(self, i, l):
        left = 2*i+1
        right = 2*i+2
        # no child
        if l <= left:
            return
        item = self.items[i]
        # only left
        if l == right:
            if self.items[i] <= self.items[left]:
                return
            self.__swap(i, left)
            return
        # both child
        l_item = self.items[left]
        r_item = self.items[right]
        if item <= l_item and item <= r_item:
            return  # item is smallest
        if item <= l_item:           # item > r_item
            self.__swap(i, right)
            self.__heapify(right, l)
            return
        if item <= r_item:           # item > l_item
            self.__swap(i, left)
            self.__heapify(left, l)
            return
        if l_item <= r_item:        # item = max, l_item = min
            self.__swap(i, left)
            self.__heapify(left, l)
            return
        else:                       # item = max, r_item = min
            self.__swap(i, right)
            self.__heapify(right, l)
            return

    # recursive pop, external access limited
    def __pop(self, i=0):
        l = len(self.items)-1
        if l < 0:
            return None
        if i == l:
            return self.items.pop(i)
        # choose left/right
        while l != 2*i+1 and l != 2*i+2:
            l = (l-1)//2
        # only left child exists
        if len(self.items)-1 == 2*i+1:
            self.__swap(i, l)
            return self.__pop(l)
        # both children exist
        dl = 1 if l == 2*i+1 else -1
        if self.items[l] <= self.items[l+dl]:
            self.__swap(i, l)
            return self.__pop(l)
        self.__swap(i, l+dl)
        self.__swap(l+dl, l)
        self.__heapify(l+dl, len(self.items))
        return self.__pop(l)
        
    def empty(self, ):
        return len(self.items) == 0

    def getMin(self, ):
        if self.empty():
            return None
        return self.items[0]

    def extractMin(self, ):
        if self.empty():
            return
        return self.__pop(0)

    def decreaseKey(self, i, val):
        l = len(self.items)
        if i >= l:
            return None
        self.items[i] = val
        while i >= 0:
            self.__heapify(i, l)
            if self.items[i] >= self.items[(i-1)//2]:
                break
            i = (i-1)//2
        return

    def deleteKey(self, i):
        if i >= len(self.items):
            return None
        self.decreaseKey(i, float("-inf"))
        return self.__pop(0)
    
    def printHeap(self):
        l = len(self.items)
        lv = 0
        print(f'{"-"*10} Heap {"-"*10}')
        while 2**lv-1 < l:
            print(f"lv {lv:2d}", end=": ")
            items = self.items[2**lv-1:min(l, 2**(lv+1)-1)]
            for item in items:
                print(f'{item:<3d}', end="")
            print('\n', end="")
            lv += 1


# for check if MinHeap is usable
h = MinHeap()
i = [1, 2, 10, 3, 4, 12, 13]
for x in i:
    h.push(x)

h.printHeap()

h.push(1)
h.printHeap()
h.push(2)
h.printHeap()

h.deleteKey(1)
h.printHeap()