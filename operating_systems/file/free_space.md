# Free Space Management

## Abstract

Along with maintaining allocated files or blocks, maintaining free space is also crucial in file management. 

### Bitmap / Bit vector

Series or collection of bits that each bit corresponds to a block. Zero(0) is used to represent allocated block, and one(1) to represent free block. They are simple and efficient. 

### Linked List

Free blocks linked as a list. I/O requests need linked list traversal. 

### Grouping

The address of free blocks are stored in the first free block. Finding of free disk is easy. 

### Counting

The entry stores the address of first free block, and a number n of free blocks after the first block. 

---

## Reference

- [Free space management](https://www.geeksforgeeks.org/operating-system-free-space-management/)