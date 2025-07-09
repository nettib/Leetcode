class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        columns = len(board[0])

        for r in range(rows):
            for c in range(columns):
                d = 0
                l = 0
                for i in range(r - 1, r + 2):
                    if i < 0 or i >= rows:
                        continue
                    for j in range(c - 1, c + 2):
                        if (i == r and j == c) or j < 0 or j >= columns:
                            continue
                        elif board[i][j] == 0 or board[i][j] == 2:
                            d += 1
                        else:
                            l += 1

                if board[r][c] == 1 and (l < 2 or l > 3):
                    board[r][c] = 3
                if board[r][c] == 0 and l == 3:
                    board[r][c] = 2
            
        print(board)
    
        for r in range(rows):
            for c in range(columns):
                if board[r][c] == 3:
                    board[r][c] = 0 
                if board[r][c] == 2:
                    board[r][c] = 1