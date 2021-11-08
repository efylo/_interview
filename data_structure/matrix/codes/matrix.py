


class Matrix:
    def __init__(self, row: int, column: int, default=int()) -> None:
        self.matrix = [[default for _ in range(column)] for _ in range(row)]
        self.row = row
        self.column = column
        pass

    def switch(self, row, column, new_val):
        if row >= self.row or column >= self.column:
            return None
        self.matrix[row][column] = new_val

    def swap(self, matrix, yx1: tuple, yx2: tuple):
        temp = matrix[yx1[0]][yx1[1]]
        matrix[yx1[0]][yx1[1]] = matrix[yx2[0]][yx2[1]]
        matrix[yx2[0]][yx2[1]] = temp

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