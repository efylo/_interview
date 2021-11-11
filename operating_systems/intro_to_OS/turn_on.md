# Turn on a computer

## Abstract

A computer firstly start up an operating system, a special program for helping other programs by controlling the computer hardware. 

### Process

1. System startup
2. Stage 1 boot loader
3. Stage 2 boot loader
4. Kernel
5. Init

### Functions

BIOS - tells a computer to look for a special program, a boot loader, which is usually located on the lowest-numbered hard disk. 

POST(Power On Self Test) - a function of BIOS, it initializes hardware devices such as RAM, CPU, and others. 

MBR(Master Boot Record) - a small program for finding the operating system. the process starts with the POST, ends when the BIOS searches for the MBR on the hard drive. 

The bootstrap loader - stored in computer's non-volatile memory. it loads the operating system from the computer into memory if POST is successful. 

init - the last step of the kernel boot sequence. it determines initial run-level of the system. then it start up various daemons for networking and other services. 

---

## Reference

- [What happens when we turn on computer?](https://www.geeksforgeeks.org/what-happens-when-we-turn-on-computer/)