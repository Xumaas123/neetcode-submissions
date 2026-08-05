class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        T = 0
        if row1 > row2: 
            temp = row1 
            row1 = row2
            row2 = temp
        if col1 > col2 : 
            temp = col1 
            col1 = col2
            col2 = temp
        for i in range(row1, row2 + 1): 
            for j in range(col1, col2 + 1): 
                T += self.matrix[i][j]
        return T

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)