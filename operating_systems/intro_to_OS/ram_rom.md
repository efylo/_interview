# Random Access Memory(RAM) and Read-Only Memory(ROM)

## Abstract

Two basic types of memory: Primary memory(RAM and ROM), Secondary memory(hard drive, CD, etc). 

Random Access Memory is primary-volatile memory, and Read-Only Memory is primary-non-volatile memory. 

### Some Classifications

RAM - Static RAM, Dynamic RAM

ROM - Programmable ROM, Erasable PROM, Electrically EPROM

---

## Random Access Memory(RAM)

- Also called read-write memory, main memory, primary memory

- Stores programs and data that the CPU requires during the execution of a program

- Volatile memory, so the data is lost when the power is off

  | DRAM                    | SRAM                            |
  | ----------------------- | ------------------------------- |
  | tiny capacitors         | D filp-flops                    |
  | a recharge every few ms | hold content if power available |
  | inexpensive             | expensive                       |
  | slower                  | faster                          |
  | many bits(4GB~)         | less bits possible              |
  | less power, heat        | more power, heat                |
  | used for main memory    | used for cache                  |

---

## Read-Only Memory(ROM)

- Stores crucial information essential to operate the system
- Not volatile, always retains its data
- Used in embedded systems, where the programming needs no change
- Used in calculators and peripheral devices
- Classifications
  1. PROM - can be programmed by the user, cannot be changed if once programmed
  2. EPROM - can be reprogrammed, need UV light exposal to erase, erase all to reprogram
  3. EEPROM - erased by an electric field, but only portions erasable
  4. MROM - Hard-wired devices containing pre-programmed set of data or instructions

---

## Table

| RAM               | ROM                         |
| ----------------- | --------------------------- |
| Temporary storage | Permanent storage           |
| Store data in MBs | Store data in GBs           |
| Volatile          | Non-volatile                |
| Normal operations | Startup process of computer |
| Faster writing    | Slower writing              |

---

## Reference

- [Random Access Memory(RAM) and Read-Only Memory(ROM)](https://www.geeksforgeeks.org/random-access-memory-ram-and-read-only-memory-rom/?ref=lbp)