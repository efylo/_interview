# Array in Different Programming Languages

## Array in C

1. *static* - fixed-size, not changeable during run-time

2. *index out of bound* is not checked

3. possible *declarations* in C

   ```c
   #include <stdio.h>
   
   int main()
   {
       // Array declaration by specifying size
       int arr1[5];
       // Array declaration by initializing elements
       int arr2[] = {1, 2, 3, 4, 5};
       // both
       int arr3[5] = {1, 2, 3, 4};	// == {1, 2, 3, 4, 0};
       // index out-of-bound
       printf("%d", arr3[6]);		// not raises an error
       
       return 0;
   }
   ```

4. different from *pointer*

   - name of array indicates the address of first element
   - can be passed like pointers

5. different from *vector* in C++

   - they are *dynamic*, and have many built-in functions

---

## Array in Python

1. need to import separate module *array* for declaration

2. *operations*

   - array(*data_type*, *value_list*)
     - initialize an array with given *data type*, and *list of values*
   - append(*x*)
     - add the *value(x)* at the end of the array
   - insert(*i*, *x*)
     - add the *value(x)* at the *i*'th position
   - pop(*i*)
     - removes the element at *i*'th position and *returns* it
   - remove(*x*)
     - remove the *first occurence* of the *value(x)*
   - index(*x*)
     - returns the index of the *first occurence* of the *value(x)*
   - reverse()
     - reverses the array

3. declarations in *python*

   ```python
   import array
   
   # init array with array values
   arr = array.array('i', [1, 2, 3, 4, 5])	# 'i' refers singed integers
   arr.append(6)	# arr == [1, 2, 3, 4, 5, 6]
   arr.index(2)	# returns 2
   arr.reverse()	# arr == [6, 5, 4, 3, 2, 1]
   arr.pop(0)		# arr == [2, 3, 4, 5, 6] / returns 1
   arr.remove(4)	# arr == [2, 3, 5, 6]
   arr.insert(2, 1)# arr == [2, 3, 1, 5, 6]
   ```

---

## References

- [Arrays in C/C++](https://www.geeksforgeeks.org/arrays-in-c-cpp/)
- [Array in Python | Set 1 (Introduction and Functions)](https://www.geeksforgeeks.org/array-python-set-1-introduction-functions/)

