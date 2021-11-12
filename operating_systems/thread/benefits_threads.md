# Benefits of Threads

## Responsiveness

As a part of an interactive application, the application has to have the interactiveness, which can be thought as responding to the user fast as possible. Consider a single-threaded Youtube, if one user watches a video, then others will not get a chance to watch. 

---

## Resource Sharing

Processes don't have shared resources, which makes more effort to execute functions that need same resources. The effort could be inter process communication (IPC) in-between processes, though passing a message or getting acquired to shared resources in threads is far more easier. 

But techniques in using shared resources must be taken care by the programmer since some unknown faults could occur due to simultaneous access to the same resource. 

---

## Economy

Since thread shares the memory space, it is far more economical than running multiple processes. Consider jobs that have the same functionality, implementing them through multiple processes makes duplication upon code section, though using threads you only have to use one code section. 

Also, creating a process and context switching between processes is far more costly than creating, context switchiing threads. 

---

## Scalability

In multi-processor architecture, a single-threaded process can only execute in a single processor. Though, multi-threaded process can run on multiple processors, so that it can increase parallelism, result in increased performance. 

---

## Reference

- [Benefits of Multithreading in Operating System](https://www.geeksforgeeks.org/benefits-of-multithreading-in-operating-system/)