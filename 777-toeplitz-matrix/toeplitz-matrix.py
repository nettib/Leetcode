class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        for r in range(1, rows):
            for c in range(1, columns):
                if matrix[r][c] != matrix[r - 1][c - 1]:
                    return False

        return True