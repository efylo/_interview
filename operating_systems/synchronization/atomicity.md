# Atomicity

## Abstract

We learn the concept of molecule and atom in chemistry. Molecules are breakable into an atom or atoms. But the atom is not breakable. (Though there are researches that atom is broken into atomic nucleus and electron, atomic nuclues is broken into neutron and proton, and neutron and proton is broken into quark. ) The concept of the atom flows into the world *Atomicity*, that describes something that is not breakable into separate parts. 

Applying the *Atomicity* into computer science, it denotes an operation that cannot be interrupted by other process, thread, or anything else. 

Even the basic operations of high-level languages are breakable into instructions. Consider *x += 1* in python. It is decomposed into (load, add, store). 

```assembly
load x10 0[x9]
add x10 x10 1
store 0[x9] x10
```

If load of thread1 and load of thread2 consequently happens, then add instruction is not done twice as intended. 

Though, you don't have to consider this for local variables in stack. 

---

## Reference

- [Atomicity](https://www.geeksforgeeks.org/g-fact-57/)