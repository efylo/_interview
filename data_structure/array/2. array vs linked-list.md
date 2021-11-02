# Array vs. Linked-list

## Features

| Features     | Array                             | Linked-list                     |
| ------------ | --------------------------------- | ------------------------------- |
| memory       | contiguous                        | separate                        |
| access       | address of first member + index   | each node has info of next node |
| spatiality   | spatially efficient               | relatively inefficient          |
| cache        | efficient cache possible          | relatively inefficient          |
| access time  | random access(fast)               | *O(n)*                          |
| flexibility  | not flexible (in C it's static)   | spatially flexible              |
| professional | modifications of certain position | insertion and deletion          |

---

## Preference

- a computation within same data type, not much insertion and deletion occurrs,
  - will probably prefer *array* than *linked-list*
- a computation where insertion and deletion frequently occurrs, 
  - will probably prefer *linked-list* than *array*
- frequent access to the component, 
  - will probably prefer *array* than *linked-list*
- wishing for dynamic data structure, 
  - will probably prefer *linked-list* than *array*, 
  - though modern languages support dynamically-allocated array

---

## References

- [Linked List vs Array](https://www.geeksforgeeks.org/linked-list-vs-array/)
- [http://cslibrary.stanford.edu/103/LinkedListBasics.pdf](http://cslibrary.stanford.edu/103/LinkedListBasics.pdf)

