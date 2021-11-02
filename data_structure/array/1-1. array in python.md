# Array in Python

## Characteristics

- ### defined as a separate module

  ```python
  import array	# import array module
  ```

  ---

- ### methods for creation, manipulation of array

  - **array(data_type, values_list)** 
    - returns an array of data_type, init by values_list, *arr = array.array(data_type, values_list)*
  - **append(x)** 
    - append x to an array, *arr.append(x)*
  - **insert(i, x)** 
    - append x to i'th position of an array, *arr.insert(i, x)*
  - **pop(i)** 
    - returns and removes i'th component of an array, *rm = arr.pop(i)*
  - **remove(x)** 
    - removes firstly occurred x, *arr.remove(x)*
  - **index(x)** 
    - returns index of firstly found x, *idx = arr.index(x)*

  ---

- ### methods (or attributes) for checking status and interfacing with a list

  - **typecode**
    - returns the datatype of an array, *arr.typecode*
  - **itemsize**
    - returns size of an array, *arr.itemsize*
  - **buffer_info()**
    - returns the address and number of elements, *arr.buffer_info()*
  - **fromlist(lst)**
    - appends list to the end of array, *arr.fromlist(lst)*
  - **tolist()**
    - transforms an array into a list and returns, *lst = arr.tolist()*

  ---

- ### automatically checks consistency

  - if the component does not fit in the *data_type*, automatically raises an *OverflowError*

  ---

- ### array of 'u', unicode char

  - quite similar to *str* in Python
  - in C, string refers to the array of *char*

---

## Why might you use Array in Python (personally)?

- since array has **good spatial locality**, computation within an array may be faster
- maybe, when you want to automatically check for **consistency** within the values inside the list

---

## Appendix(type_code)

| Type Code | C Type             | Python Type       | Minimum size in Bytes |
| :-------: | ------------------ | ----------------- | --------------------- |
|    'b'    | signed char        | int               | 1                     |
|    'B'    | unsigned char      | int               | 1                     |
|    'u'    | Py_UNICODE         | unicode character | 2                     |
|    'h'    | signed short       | int               | 2                     |
|    'H'    | unsigned short     | int               | 2                     |
|    'i'    | signed int         | int               | 2                     |
|    'I'    | unsigned int       | int               | 2                     |
|    'l'    | signed long        | int               | 4                     |
|    'L'    | unsigned long      | int               | 4                     |
|    'q'    | signed long long   | int               | 8                     |
|    'Q'    | unsigned long long | int               | 8                     |
|    'f'    | float              | float             | 4                     |
|    'd'    | double             | float             | 8                     |

---

## References

- [Array in Python | Set 1 (Introduction and Functions) - GeeksforGeeks](https://www.geeksforgeeks.org/array-python-set-1-introduction-functions/)

- [Array in Python | Set 2 (Important Functions)](https://www.geeksforgeeks.org/array-in-python-set-2-important-functions/)

- [array — Efficient arrays of numeric values — Python 3.10.0 documentation](https://docs.python.org/3/library/array.html#module-array)

