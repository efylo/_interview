#Remote Procedure Call (RPC)

## Abstract

RPC is a powerful technique in construction of distributed, client-server based applications. The word *remote* refers to the fact that called procedure (object) need not have to exist in the same address space with the calling procedure (subject). 

---

## Process of RPC

| No.  | Caller (client)  |      | Callee (server)     |
| ---- | ---------------- | :--: | ------------------- |
| 1    | request message  |  >>  | wait for request    |
| 2    | wait for reply   |      | execute the request |
| 3    | resume execution |  <<  | send reply          |

0. Callee, server waits for the request of caller, client. 

1. Caller requests message to the server. 

   1-1. Caller waits for the reply.

2. Callee executes the request.

3. Callee sends reply to the client.

4. Caller resumes the execution.

---

## Structure

| Tier | Caller (client) | Callee (server) |
| ---- | --------------- | --------------- |
| 1    | Client          | Server          |
| 2    | Client stub     | Server stub     |
| 3    | RPC runtime     | RPC runtime     |

### Flow

1. Client - Client stub - RPC(client) - RPC(server) - Server stub - Server
2. Server - Server stub - RPC(server) - RPC(client) - Client stub - Client

---

## Issues

### RPC Runtime

RPC run-time system refers to a library of the network communications. e.g) socket library in python. The system offers binding, communication over appropriate protocol, pass call data between the client and server, and handle communication errors. 

### Stub

Stubs provide transparency to the programmer-written application code. Stubs deal with making data into protocol-appropriate data type, call RPC run-time protocols. 

### Binding

Binding is the process about how and where to search for the server from the client. 

### The call semantics - RPC

- Retry request message
- Duplicate filtering
- Retransmission of results

---

## Advantages

1. RPC offers *Abstraction*
2. RPC may have many *protocol layers* for improving performance
3. RPC enables the use of applications in *distributed environment*
4. RPC code makes *re-writing / re-developing minimized*
5. RPC support *process-oriented*, *thread-oriented* models

---

## Reference

- [Operating System | Remote Procedure call (RPC)](https://www.geeksforgeeks.org/operating-system-remote-procedure-call-rpc/)