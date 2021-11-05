# class Item with item value, and priority
class Item:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
    
    # method for comparing priority
    def isPriorTo(self, new_item):
        return self.priority <= new_item.priority
    
    def __repr__(self, ):
        return f'[item={self.item}, priority={self.priority}]'


# Priority Queue class
# insert(item, priority) -> None
# getHighestPriority() -> return the highest priority item
# deleteHighestPriority() -> remove the highest priority item
class PriorityQueue:
    def __init__(self) -> None:
        self.items = []
    
    # swap both item and priority
    def __swap(self, a, b):
        temp = self.items[a]
        self.items[a] = self.items[b]
        self.items[b] = temp
    
    # priority queue insert
    def insert(self, item, priority):
        item = Item(item, priority)
        self.__push(item)
    
    # recursive push, without external access
    def __push(self, item: Item, i: int = 0):
        l = len(self.items)
        if i == l:
            self.items.append(item)
            return
        # choose left/right, i has to be initially 1 to fit the algorithm
        while l != 2*i+1 and l != 2*i+2:
            l = (l-1)//2
        # i'th priority is prior to given item's priority
        if self.items[i].isPriorTo(item):
            self.__push(item, l)
            return
        # given item's priority is prior to i'th priority
        old_item = self.items[i]
        self.items[i] = item
        self.__push(old_item, l)
        return
    
    # assumption: both children are heapified, if not fail
    def __heapify(self, i, l):
        left = 2*i+1
        right = 2*i+2
        # no child - no need for heapification
        if l <= left:
            return
        item = self.items[i]
        l_item = self.items[left]
        # only left child
        if l == right:
            if item.isPriorTo(l_item):
                return
            self.__swap(i, left)
            return
        # both child exists
        r_item = self.items[right]
        item_prior_l = item.isPriorTo(l_item)
        item_prior_r = item.isPriorTo(r_item)
        # item is prior to left, right
        if item_prior_l and item_prior_r:
            return
        # item is only prior to left
        if item_prior_l:
            self.__swap(i, right)
            self.__heapify(right, l)
            return
        # item is only prior to right
        if item_prior_r:
            self.__swap(i, left)
            self.__heapify(left, l)
            return
        if l_item.isPriorTo(r_item):    # item = min, left = most prior
            self.__swap(i, left)
            self.__heapify(left, l)
            return
        self.__swap(i, right)           # item = min, right = most prior
        self.__heapify(right, l)
        return

    # recursive pop, external access limited
    def __pop(self, i=0):
        l = len(self.items)-1
        if l < 0:
            return None
        if l == i:
            return self.items.pop(i)
        # choose left/right
        while l != 2*i+1 and l != 2*i+2:
            l = (l-1)//2
        # only left child
        if len(self.items)-1 == 2*i+1:
            self.__swap(i, l)
            return self.__pop(l)
        # both child exist
        dl = 1 if l == 2*i+1 else -1
        if self.items[l].isPriorTo(self.items[l+dl]):
            self.__swap(i, l)
            return self.__pop(l)
        self.__swap(i, l+dl)
        self.__swap(l+dl, l)
        self.__heapify(l+dl, len(self.items))
        return self.__pop(l)
    
    def empty(self, ):
        return len(self.items) == 0
    
    def getHighestPriority(self, ):
        if self.empty():
            return
        return self.items[0].item
        
    def __decreaseKey(self, i, val):
        l = len(self.items)
        if i >= 1:
            return
        self.items[i].priority = val
        while i >= 0:
            self.__heapify(i, l)
            if self.items[i].priority >= self.items[(i-1)//2].priority:
                break
            i = (i-1)//2
        return
    
    def deleteHighestPriority(self, ):
        if self.empty():
            return
        prev_priority = self.items[0].priority
        self.__decreaseKey(0, float("-inf"))
        item = self.__pop(0)
        item.priority = prev_priority
        return item
    
    
def main():
    a = Item('a', 3)
    b = Item('b', 2)
    c = Item('c', 1)
    d = Item('d', 1)
    e = Item('e', 3)
    f = Item('f', 0)

    X = [a, b, c, d, e, f]

    pq = PriorityQueue()

    for x in X:
        pq.insert(x.item, x.priority)
    
    print(pq.items)
    print(f'the highest priority item: {pq.getHighestPriority()}')
    print(f'delete the highest priority item: {pq.deleteHighestPriority()}')
    print(f'after deletion')
    print(pq.items)


if __name__ == "__main__":
    main()