class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(row + 1, cols):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        for row in range(rows):
            l, r = 0, cols - 1
            while l <= r:
                matrix[row][l], matrix[row][r] = matrix[row][r], matrix[row][l]
                l += 1
                r -= 1
