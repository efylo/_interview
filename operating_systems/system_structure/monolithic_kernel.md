# Monolithic Kernel

## Abstract

In contrast to a microkernel, monolithic kernel implements user services and kernel services in the samd address space. Monolithic kernel provides CPU scheduling, memory management, file management, and other operating system functions through system calls. (More functions provided than a microkernel.) Since it uses the same address space, the execution of the OS is faster. Though, the system have to be carefully monitored since the entire system crashes if any service fails. 

---

## Pros/Cons

### Pros

- It provides CPU scheduling, memory management, file management and other OS functions through system calls. 
- A single large process runs entirely in a single address space. 
- A single static binary file, e.g) Unix, Linux, etc

### Cons

- If any service fails, it leads to an entire system failure
- If the user has to add any new service, the entire operating system needs modification

---

## Reference

- [Monolithic Kernel and key differences from Microkernel](https://www.geeksforgeeks.org/monolithic-kernel-and-key-differences-from-microkernel/)