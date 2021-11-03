# Linked List

## Abstract

A linked list is a linear data structure, not contiguously located in memory. Structured with a data(key) and a pointer to next. So, it needs head and tail(NULL) to designate the start and end of the list. In contrast, array only need a pointer to point out the structure. 

---

## Features

### Pros

- dynamic in size, allocation
- ease in insertion/deletion

### Cons

- linear access, O(n)
- extra memory space for a pointer
- not cache friendly

---

## in Python

recursive deletion method not possible(for me)

- since python does not support direct access to the address(via pointer), and recursive deletion method needs manipulation upon the address of node to delete. 

- though if you implement node to direct previous node, which is doubly linked list, recursive deletion can be made possible. 

- e.g. code)

  ```python
  # a simple Node class
  class Node:
      def __init__(self, key):
          self.key = key
          self.next = None
  
  head = Node(1)      # a node of key(1)
  tail = Node(2)      # a node of key(2)
  head_id = id(head)  # memory addr of head
  tail_id = id(tail)  # memory addr of tail
  head = tail         # assertion(tail->head)
  print(f'head id before assertion: 0x{head_id:x}')
  print(f'tail id before assertion: 0x{tail_id:x}')
  print(f'head id after assertion: 0x{id(head):x}')
  
  # head id before assertion: 0xff00 (just for example)
  # tail id before assertion: 0xff88
  # head id after assertion: 0xff88
  # => variable 'head' now points the address of 'tail'
  # assertion to certain memory address is banned
  ```

why?

- since direct access to certain memory address is not secure
- attacks on PC is probable with direct memory access via pointer

---

## Code

- [LinkedList class definition](./codes/linkedlist.py)

---

## Reference

- [Linked List | Set 1 (Introduction)](https://www.geeksforgeeks.org/linked-list-set-1-introduction/)

- [Linked List | Set 2 (Inserting a node)](https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/)

- [Linked List | Set 3 (Deleting a node)](https://www.geeksforgeeks.org/linked-list-set-3-deleting-node/)

