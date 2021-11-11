# Kernel I/O Subsystem in OS

## Abstract

Many services related to I/O is provided by the kernel. They include scheduling, caching, spooling, device reservation, and error handling. The I/O subsystem also includes protection from errant processes and malicious users. 

---

## I/O Subsystem

1. I/O Scheduling

   Scheduling a set of I/O request means to determine a good order in execution. FIFO is the best choice. Scheduling also improves performance, fairness, and reduces waiting, response, and turnaround time. A wait queue is implemented to schedule the request. 

2. Buffering

   Buffer is a memory area, stores data that is transferred between two devices or a device and an application. Three reasons for buffering are, coping with a speed mismatch of a data stream, providing adaptation for data of different sizes, and supporting copy semantics. 

3. Caching

   Cache is a region of fast memory holding a copy of data. Buffer can hold the existing copy of a data item, though cache holds a copy that resides elsewhere. 

4. Spooling and Device Reservation

   A spool is a buffer holding the output of a device. The spooling system queues the spool files in a separate disk file so that outputs does not get mixed. 

5. Error Handling

   Guard against hardware and application errors. 

6. I/O Protection

   For protection against I/O accesses, all I/O instructions are privileged. 

---

## Reference

- [Kernel I/O Subsystem in Operating System](https://www.geeksforgeeks.org/kernel-i-o-subsystem-in-operating-system/)