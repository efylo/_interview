# Hashing

## Abstract

a technique or process of mapping keys, values into the hash table by using a hash function. 

hashing makes access to elements faster, whose speed depends on the efficiency of the hash function. 

making hash table using arrays, linked lists, or even binary search tree is inappropriate since their insertion, deletion, and search depends on the size of data structure. 

using direct access table may best fits the means of 'hashing'. though, direct access table uses lots of memories since keys can occupy lots of memory spaces. 

a better way is using hash function, and hash table. 

hash function converts a key into small practical value (maybe integer). converted value is then used as an index of hash table. good hash function has two properties, which are efficiency in computation and unifom distribution of the keys. 

hash table stores pointers to records, corresponding to the given values converted through hash function. they have to handle collisions since hash function diminishes the size of a key, which may violates one-to-one correspondence. 

one-to-one correspondence can be multiple keys with same pointer, or a key corresponding to multiple pointers. 

---

## In Python

in Python, you can use hashing via built-in dictionary data structure. since their search is apparently faster than python list, I use them frequently in solving for coding tests of IT companies (or of SW groups). though python built-in dictionary data structure can raise an error if there is no corresponding key, these limitations can be solved by using defaultdict class of collections module. 

since a key should not change, they have to be immutable object. this is why python doesn't approve a key of list, dict, etc. if you want to use a key of some list of values, you'd rather use tuple instead. 

a defaultdict class of collections module does not raise an error even though you assert a key not in hash table. they rather returns default value (e.g. int(), list(), etc). if you want a dictionary of lists, I'd rather recommend using defaultdict since you don't have to check every key to append a value to the list. 

though, you'd rather be careful when saving a pointer inside a dictionary. python dictionary doesn't check if there are multiple keys with same pointer or not. 

```python
from collections import defaultdict
# automatic creation of list
y = defaultdict(list)
for i in range(4):
    y['a'].append(2*i)    # [0, 2, 4, 6]
    y['b'].append(2*i+1)  # [1, 3, 5, 7]
# violates one-to-one correspondence
x = dict()
default = []
for i in range(4):
    if i == 0:
        x['a'] = default
        x['b'] = default
    x['a'].append(2*i)
    x['b'].append(2*i+1)    # [0, 1, 2, 3, 4, 5, 6, 7]
```

---

## Reference

- [Hashing Data Structure](https://www.geeksforgeeks.org/hashing-data-structure/)
- [Hashing | Set 1 (Introduction)](https://www.geeksforgeeks.org/hashing-set-1-introduction/)

