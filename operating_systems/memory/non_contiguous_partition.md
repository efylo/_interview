# Non-Contiguous Allocation

## Abstract

Before allocating memory to a process, the process is separated and acquires its virtual address. Virtual address corresponds to physical address of the memory, and maintaining relationships can be done through *paging* and *segmentation*. *Page table* is the table which has the relationships of virtual and physical address. Since address is maintained in virtual state, it is possible to have the virtual address of process's data which violates the boundary of physical memory. This is called *Spanning*. 

Though, there exist extra overload in matching between virtual address and physical address. This work is done through maintaining page table. 

For further understanding of non-contiguous allocation, have to check through how *paging* and *segmentation* work 

---

## Reference

- [Non-Contiguous Allocation in Operating System](https://www.geeksforgeeks.org/non-contiguous-allocation-in-operating-system/)