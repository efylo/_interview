# Functions of OS(1)

## Abstract

OS works as an interface between the user and the computer hardware. So, the purpose of OS is providing an environment for the user to execute programs conveniently, efficiently. 

Such tasks are mainly focused on the management of the allocation of the computer hardware. Tasks include guaranteeing correctness, preventing the user programs not to interfere the proper working of the system. (User programs not to make failure to the system)

### Specific Tasks

- The allocation of memory, devices, processors, and information
- Programs for the first task
  1. Traffic controller
  2. Scheduler
  3. Memory management module
  4. I/O programs
  5. File sysem

Above contents are frequently mentioned in the introduction to OS in geeksforgeeks. 

---

## Important Functions of an OS

1. Security 
   - protect user data, prevent unauthorized accesses
2. Control over system performance
   - monitor system health for improving performance
   - log on the response time, used for troubleshooting programs
3. Job accounting
   - track time, resources by various tasks, users
4. Error detecting aids
   - constant monitor upon the system, avoiding malfunctions
5. Coordination between other software and users
   - coordinate and assign interpreters, compilers, assemblers, and other SW to various users
6. Memory management
   - keep track of main memory, a table of a program and its address
   - manages multiprogramming, deciding the process to grant access for a certain time
   - allocate and deallocate the memory to a process
   - deallocation when process is terminated or performing I/O
7. Processor management
   - Memory for 'where', processor for 'when' or maybe the order
   - as a traffic controller, keep track of the status of the processes
   - allocates the CPU to a process, deallocates when process not required
8. Device management
   - keep track of all devices connected to the system
   - designates I/O controller for every device
   - decides the process which gets access to a certain device for how long
9. File management
   - keep track of where information is stored, user access settings, status, etc

### Main memory

A term 'memory' in memory management refers main memory of the computer. Most will know if I call this as RAM or Rapid Access Memory. 

It is a large array of words, where each word have its own address. They are fast, support direct access by the CPU. For the execution of the program, it has to be loaded in the main memory. 

---

## Services

1. Program execution
   - responsible for efficient execution of programs
2. Handling I/O operations
   - handling all sort of inputs (or interfaces)
3. Manipulation of file system
   - making decisions how the data is manipulated and stored
4. Error detection and handling
   - detecting any type of error or bugs
5. Resource allocation
   - the proper use of all the available resources
6. Accounting(회계, 기록을 남기는 것)
   - tracks an account of all the functionalities
7. Information and resource protection
   - using available info, resources in the most protedted way

---

## Reference

- [Functions of Operating System](https://www.geeksforgeeks.org/functions-of-operating-system/)