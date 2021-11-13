# Memory Hierarchy

## Abstract

Sometimes, I think hierarchical, pyramidal way of organizing things is quite natural. For example, society is organized in a way of pyramids. Like 20% of people takes 80% of wealth (quite an old phrase, anyway), though pyramid-like hierarchy can burdensome more load to each. Also human brain processes the information in that kind of way, in a form of long-term memory and short-term memory. 

So, computer memory in a form of pyramid-like hierarchy is one of the most efficient way of organizing the data. 

| Level | Component                | Description                     |
| ----- | ------------------------ | ------------------------------- |
| 0     | CPU Register             | Highest cost / bit, performance |
| 1     | Cache Memory (SRAMs)     |                                 |
| 2     | Main Memory (DRAMs)      |                                 |
| 3     | Magnetic Disk (HDD, SSD) | Highest capacity / access time  |

We don't usually use optical disk and magnetic tape in a computer, they are the cheapest memory possible. 

---

## Types

1. *External Memory* / *Secondary Memory*

   HDD, SSD - They are only accessable through I/O Module. 

2. *Internal Memory* / *Primary Memory*

   Main, Cache Memory / CPU registers - They are directly accessable by processor

---

## Terms

1. *Memory* - made up of registers, with each register has its location. 
2. *Address* - memory locations
3. *Capacity* - the total number of bit a memory can store
4. *Cell* - a storage element
5. *Word* - a group of bits
6. *byte* - group of 8 bits

---

## Reference

- [Memory Hierarchy Design and its Characteristics](https://www.geeksforgeeks.org/memory-hierarchy-design-and-its-characteristics/)
- [Introduction to memory and memory units](https://www.geeksforgeeks.org/introduction-to-memory-and-memory-units/)