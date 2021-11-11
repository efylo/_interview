# Intro - OS

## Abstract

An operating system = an intermediary between the user and computer hardware. 

- provides an environment for the user to execute the programs conveniently, efficiently. 
- a software for the management of computer hardware. 

---

## Definition

- as a program: controls the execution of application programs
- as an interface: between the user and the hardware
- as a kernel: the program which is always on the computer

### Concerns of OS

- the allocation of resources and services (memory, processors, devices, and info.)
- OS includes programs to manage the resources

### Included Programs (Generally)

- a traffic controller
- a scheduler
- a memory management module
- I/O programs
- a file system

---

## Functions

### As a performance 

- convenience, efficiency, ability to evolve, and throughput

### As a management

- resource: control multiple user accesses
- process: scheduling, termination of the process
- storage: the file system mechanisms, (NIFS, CFS, CIFS, NFS, etc.)
- memory: primary memory - keep track, decide allocation, deallocations
- security/privacy: prohibit unauthorized applications, accesses

### As an user interface 

- [User, System/application programs, OS, Hardware]

### Purposes

- controls the allocation, use of system resources among various users and tasks
- an interface between the hardware and the programmer

### Tasks

- the facilities to create, modification of programs and data files through an editor
- access to the compiler - translates high-level language to machine language
- a loader program - move the program to the computer's memory for execution
- routines for handling the details of I/O programming

---

## Modules

### I/O System Management

It keeps track of the status of devices, a.k.a I/O traffic controller. Each I/O device has its own device handler. Subsystems include a memory management for buffering, caching, and spooling and a device driver interface. 

### Assembler

Inputs an assembly language program, outputs an object program with the information for the loader to prepare the execution. The programmer would make fundamental instructions of ones and zeros, place them inside the memory of the machine. 

### Compiler

The compiler (or interpreter) processes the high-level languages. A compiler compiles a source high-level program into an object program. And an interpreter executes a source program as if it is a machine language. 

### Loader

Loader loads an object program, and prepare for the execution. Some loading schemes include absolute, relocating, direct-linking, etc. A word 'load' means the placement of a program into memory. 

---

## Terms

- Hardware: includes memory, CPU, ALU, I/O devices, peripheral devices, and storages
- System program: compilers, loaders, editors, OS, etc. 
- Application program: business programs, database programs
- Storage: a disk, includes hard disk(HDD), solid-state device(SSD)
- Memory: main memory, RAM

---

## Reference

- [Introduction of Operating System](https://www.geeksforgeeks.org/introduction-of-operating-system-set-1/)

