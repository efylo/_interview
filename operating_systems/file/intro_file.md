# File Management

## Abstract

A file is *a collection of related information* stored in secondary storage(disk). It can be *a collection of logically related entities*. In user's view, it is the smallest allotment of logical secondary storage. 

---

## About Files

- **The Name**

  name.extension

- **Attributes**

  Name, Type, Size, Creation Data, Author, Last Modified, protection

- **Operations**

  Create, Open, Read, Write, Append, Truncate, Delete, Close

  *Append*: add data to last of the file

  *Truncate*: resize the file

- **Types**

  Executable, Object, Source Code, Batch, Text, Word Processor, Archive, Multimedia, Markup, Library, Print or View

  *Executable*: Run machine language program

  *Object*: Compiled, but machine language not linked

  *Batch*: Commands to the command interpreter

---

## File Directories

A file directory is a collection of files. Below are the information and operations of the file directory. 

- **Information**

  Name, Type, Address

  Current length, Maximum length

  Date last accessed, Date last updated

  Owner id, Protection info. 

- **Operation**

  Search for a file, Create a file, Delete a file, List a directory

  Rename a file, Traverse the file system

Those attributes of file directories benefits in *efficiency*, *naming*, *grouping*

- **Types**

  *Single-level Directory*: Only 1-level exists

  *Two-level Directory*: Separate directories each exist for multiple users

  ***Tree-Structured Directory***: Directory as a form of a tree, efficient in search, grouping possible

---

## File Allocation

### File Allocation Methods

- **Continuous Allocation**

  Continuous blocks is allocated to a single file. 

- **Linked Allocation**

  Allocation on an individual block, each block contains a pointer to the next block. 

- **Indexed Allocation**

  Maintainence on *the file allocation table*, allocation could be fixed or variable-sized. 

### Disk-Free Space Management

To manage, or maintain space in the disk not currently allocated. 

- **Bit Tables**

  A vector containing one bit for each block on the disk, which 0 = free block, 1 = allocated block

- **Free Block List**

  The list of the numbers of all free blocks is maintained

---

## File Access

Three ways in accessing a file - *Sequential Access*, *Direct Access*, *Index sequential Method*

- **Sequential Access**

  The simplest access method, the data is processed *in order*. Far most common method in editor and compiler. 

- **Direct Access**

  a.k.a *relative access method*, read a block in a sequence of *relative block number*

- **Index Sequential Method**

  Constructs an index for the file, which contains the pointer to blocks. 

---

## Reference

- [File Systems in Operating System](https://www.geeksforgeeks.org/file-systems-in-operating-system/)
- [File Access Methods in Operating System](https://www.geeksforgeeks.org/file-access-methods-in-operating-system/)