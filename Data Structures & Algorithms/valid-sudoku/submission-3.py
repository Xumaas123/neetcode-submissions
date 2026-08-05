class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        R  = []
        n = len(board)
        for i in board : 
            for j in i : 
                if j == '.' : 
                    continue
                elif j in R : 
                    return False
                R.append(j)
            R = []
        R = []
        for i in range(n) : 
            for j in range(n) : 
                if board[j][i] == '.': 
                    continue
                elif board[j][i] in R : 
                    return False
                R.append(board[j][i])
            R = []
        start_row = [0,3,6]
        start_col = [0,3,6]
        for r in start_row : 
            for c in start_col:
                R = []
                for i in range(r, r + 3) : 
                    for j in range(c , c + 3): 
                        if board[i][j] == '.' : 
                            continue
                        elif board[i][j] in R :
                            return False
                        R.append(board[i][j])
        return True