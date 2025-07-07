class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        columns = len(mat[0])

        diff = columns - 1

        total = 0

        for r in range(rows):
            for c in range(columns):
                if r == c or r + c == diff:
                    total += mat[r][c]

        return total