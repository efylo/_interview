# Microkernel in OS

## Abstract

Kernel is the core part of an OS, manages system resources. It's a bridge between the application and hardware of the computer. Also, kernel is one of the first loaded programs on start-up, after the bootloader. 

---

## Kernel Mode

In kernel mode, the CPU is allowed to execute only certain instructions, a.k.a privilege instruction. Privilege instructions allow the implementation of special operations. The execution of special operations makes the interface between the functions of the OS or activity of another user program and the user program. 

- The OS puts the CPU in kernel mode for special operations
- The OS puts the CPU in user mode when a user program is in execution, can't interface with the OS program
- User-level instructions don't require special privileges

---

## System call

System call is called from the user process to execute special operations in the kernel mode. They are typically implemented in the form of software interrupts, which make the OS to switch the mode bit to kernel mode. 

The attempts to execute illegal instructions are captured by the OS since they generate software interrupts. Then the OS issues an error message, and probably terminates the offending program. 

---

## Microkernel

Microkernel is one of the classifications of the kernel. A kernel manages all of the system resources, though a microkernel implements the user services and kernel services in different address spaces. It can be understood as an isolation between user-based and kernel-based services. This mechanism reduces the kernel size, which then reduces the size of an OS. 

Likewise, the communication between user program, application and services in user address space could be done through passing a message. Since user programs don't really affect kernel mode, the OS will not be affected even though user services fail. 

Also, the concept of isolation makes kernel easily extendable, portable, secure, and reliable. Thus, we can possibly say that the most important services of the kernel mode is done through a microkernel, and the services that are not so important are done through the system application. 

The Microkernel is responsible for: 

- Inter Process-Communication(IPC)
- Memory Management
- CPU-Scheduling

Advantages of using the Microkernel are:

- The architecture is small and isolated, thus functions better
- Expansion of the system is easier, can be done without disturbing the kernel

---

## Reference

- [Microkernel in Operating Systems](https://www.geeksforgeeks.org/microkernel-in-operating-systems/)
