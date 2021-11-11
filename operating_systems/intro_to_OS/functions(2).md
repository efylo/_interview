# Functions of OS(2)

## The Goal

The fundamental goal is to execute user programs, and to make tasks easier. There exists various application programs along with hardware systems which are used to perform the works. 

OS, is a software for the management and control of the entire set of resources and for the effective utilization of every part of a computer. 

- User: User communicates with system & application programs
- Programs: they communicate with users, on top of the OS
- OS: it manages whole programs, and the hardware

---

## Needs

- A platform for Application programs

  OS provides a platform - where application programs can run.

- Managing Input-Output unit

  The computer has multiple resources - memory, monitor, etc.

  It is the OS which manages them, is responsible for effective utilization.

- Consistent UI

  For a platform, the OS provides user interface, or templates for UI

- Multitasking

  OS manages memory, allows multiple programs on its resources, programs can also communicate each other through shared memory

---

## Functions

- Processor Management

  It deals with the management of the CPU. The OS controls the allotment of CPU time to different processes, and it is called scheduling. Some scheduling techniques include SJF, RR, Priority-Based scheduling, etc. 

- Device Management

  The OS communicates with the hardware and the attached devices, balances between them and the CPU. This is needed because processing speed is different (CPU is much faster). Techniques such as buffering ans spooling are used for device management. 

- Buffering

  Buffer is for temporal storing of input and output data. The data from the input / for the output device is send to the input / output buffer respectively. The OS takes control of the buffers. Also the situation when the buffer is full or empty is informed by the OS. 

- Spooling(Simultaneous Peripheral Operation on Line)

  Spooling is the technique to manage processing of different tasks on the same input/output device. The OS stores the data of every user, processes one by one. 

- Memory management

  The CPU and I/O device both interact with the memory. A program, for example, needs to be loaded onto the memory and takes up space until it is completed. Then the memory space is freed, now available to other programs. It is not an easy process since there exist lots of possibilities about how the available memory is located. These are done through Partitioning, and Virtual memory. 

- Partitioning

  The total memory (maybe 4, 8, 16GB) is divided into the same size(pages), or different sizes(segments). Due to fragmentation, efficient way of partitioning have to be considered. 

- Virtual Memory

  Using this technique, the OS can provide users to load programs larger than the main memory of the computer. The execution of the program is done even if not all of the program is loaded onto the main memory. 

- File Management

  Using File Allocation Table(FAT), the OS can keep the information of any data on a computer. Inside the FAT, there exists filename, type, size, starting address, access mode, etc. 

  The OS is capable of creating, editing, copying, allocating memory, and updating the FAT. 

---

## Reference

- [Need and Functions of Operating Systems](https://www.geeksforgeeks.org/need-and-functions-of-operating-systems/)