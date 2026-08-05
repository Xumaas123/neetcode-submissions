class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        T_row = len(matrix[0])
        T_column = len(matrix) 

        T = [[0] * T_column for _ in range(T_row)]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                T[j][i] = matrix[i][j]
        return (T)