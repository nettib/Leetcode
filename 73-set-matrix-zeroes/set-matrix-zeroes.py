class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # rows = [1] * len(matrix)
        # columns = [1] * len(matrix[0])
        left = 1

        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                if matrix[row][column] == 0:
                    matrix[row][0] = 0
                    if column == 0:
                        left = 0
                    else:
                        matrix[0][column] = 0
        

        for row in range(len(matrix) - 1, -1, -1):
            for column in range(len(matrix[row]) - 1, -1, -1):
                if column == 0:
                    if matrix[row][0] == 0 or left == 0:
                        matrix[row][column] = 0
                else:
                    if matrix[row][0] == 0 or matrix[0][column] == 0:
                        matrix[row][column] = 0
            
        