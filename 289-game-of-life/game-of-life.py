class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        columns = len(board[0])

        change1 = []
        change2 = []

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
                        elif board[i][j] == 0:
                            d += 1
                        else:
                            l += 1

                if board[r][c] == 1 and (l < 2 or l > 3):
                    change1.append(r)
                    change2.append(c)
                if board[r][c] == 0 and l == 3:
                    change1.append(r)
                    change2.append(c)

    
        for i in range(len(change1)):
            r = change1[i]
            c = change2[i]
            board[r][c] = 0 if board[r][c] == 1 else 1