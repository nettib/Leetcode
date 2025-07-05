class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        if rows == cols:
            for row in range(rows):
                for col in range(row + 1, cols):
                    matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]

            return matrix

        tran = [[0] * rows for _ in range(cols)]

        for row in range(rows):
            for col in range(cols):
                tran[col][row] = matrix[row][col]

        return tran