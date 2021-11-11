# Intro to System Call

## Abstract

A system call is the programmatic way in which a computer program request a service from the kernel of the OS it is executed on. Also, it is a way for programs to interact with the operating system. They provide the services of the operating system to the user via API. The kernel system can only be entered through a system call. For programs needing resources, system calls must be used. 

---

## Services

1. Process creation and management
2. Main memory management
3. Fild access, directory and file system management
4. Device handling(I/O)
5. Protection
6. Networking, etc

---

## Types

1. Process control: end, abort, terminate, allocate and free memory
2. File management: create, open, close, delete, read file, etc
3. Device management
4. Information maintenance
5. Communication

---

## Examples

|                         | Windows                                                      | Unix                             |
| ----------------------- | ------------------------------------------------------------ | -------------------------------- |
| Process Control         | CreateProcess(), ExitProcess(), WaitForSingleObject()        | fork(), exit(), wait()           |
| File Manipulation       | CreateFile(), ReadFile(), WriteFile(), CloseHandle()         | open(), read(), write(), close() |
| Device Manipulation     | SetConsoleMode(), ReadConsole(), WriteConsole()              | ioctl(), read(), write()         |
| Information Maintenance | GetCurrentProcessID(), SetTimer(), Sleep()                   | getpid(), alarm(), sleep()       |
| Communication           | CreatePipe(), CreateFileMapping(), MapViewOfFile()           | pipe(), shmget(), mmap()         |
| Protection              | SetFileSecurity(), InitializeSecurityDescriptor(), SetSecuriyDescriptorGroup() | chmod(), umask(), chown()        |



---

## Reference

- [Introduction of System Call](https://www.geeksforgeeks.org/introduction-of-system-call/)