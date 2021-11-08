# Matrix

## Abstract

Always thinking of matrix as a mathematical concept, it can be also interpreted as one of the data structures. 

A matrix is a collection of numbers arranged in an order of rows and columns. 

An element of the matrix can be accessed by row and column number. 

---

## Implementation

### Possible errors in implementation

In python, multiplication between a list and an integer is supported. Though, these are not recommended in a list of mutable objects. 

Below is a code that shows dangers in multiplication between a list of lists and an integer. I really don't know internal procedures that goes behind this faults. But I understood this that python multiplication between a list and an integer just copies the elements that are really inside the list. So, what it means that it is not 'list' exists inside the list, but rather it's 'pointer' that really lies inside. 

#### Example codes

```python
# define a list of 3 lists
x = [[]] * 3
# appending 1 to 0'th list of x
x[0].append(1)
# print: [[1], [1], [1]]
print(x)

# rather, define using a simple generator
x = [[] for _ in range(3)]
# appending 1 to 0'th list of x
x[0].append(1)
# print: [[1], [], []]
print(x)
```

These are errors that I think is quite probable when implementing matrix as a list of lists. You might use a simple generator to define a list of lists or use class with confined number of rows and columns instead. 

### Class Matrix

Below are implementation of matrix class on my own. I've implemented recursive way of rotating a matrix, and quite costly way of matrix multiplication. 

```python
class Matrix:
    def __init__(self, row: int, column: int, default=int()) -> None:
        self.matrix = [[default for _ in range(column)] for _ in range(row)]
        self.row = row
        self.column = column
        pass
    
    # add new element to the matrix
    def switch(self, row, column, new_val):
        if row >= self.row or column >= self.column:
            return None
        self.matrix[row][column] = new_val
    
    # swap two elements of matrix
    def swap(self, matrix, yx1: tuple, yx2: tuple):
        temp = matrix[yx1[0]][yx1[1]]
        matrix[yx1[0]][yx1[1]] = matrix[yx2[0]][yx2[1]]
        matrix[yx2[0]][yx2[1]] = temp

    # rotating self.matrix
    def rotate(self, ):
        self.matrix = self.__rotate(self.row, self.column, self.matrix)
        temp = self.row
        self.row = self.column
        self.column = temp
        
    # recursive algorithm for rotation of matrix
    def __rotate(self, y, x, matrix):
        if y == 1:
            return [[ele] for ele in matrix[0]]
        if x == 1:
            return [[ele[0] for ele in matrix]]
        m = min(y, x)
        for r in range(m):
            for j in range(r+1, m):
                self.swap(matrix, (r, j), (j, r))
        if y == x:
            return matrix
        if y > x:
            mat2 = self.__rotate(y-x, x, matrix[x:])
            return [matrix[i][:x]+ mat2[i] for i in range(x)]
        mat1 = [matrix[i][:y] for i in range(y)]
        mat2 = self.__rotate(y, x-y, [matrix[i][y:] for i in range(y)])
        return mat1 + mat2
	
    # overrides multiplication method
    def __mul__(self, other):
        if self.column != other.row:
            return None
        other.rotate()
        ret = []
        for i in range(self.row):
            ret.append(list())
            for j in range(other.row):
                sum_ = 0
                for k in range(self.column):
                    sum_ += self.matrix[i][k]*other.matrix[j][k]
                ret[i].append(sum_)
        return ret

A = Matrix(3, 4)
A.matrix = [[1, 2, 3, 4], [0, 1, 2, 3], [2, 3, 4, 5]]
B = Matrix(4, 2)
B.matrix = [[1, 2], [3, 4], [2, 3], [4, 5]]

print(A*B)
# [[29, 39], [19, 25], [39, 53]]
```

Methods I've used are quite brute-force, though works fine. Python's external library 'numpy' is frequently used in dealing with matrix computations. They would probably provide you the fastest way in manipulating the matrix. 

---

## Reference

- [Matrix Archives](https://www.geeksforgeeks.org/matrix/)