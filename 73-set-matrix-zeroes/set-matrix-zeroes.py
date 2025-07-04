class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = [1] * len(matrix)
        columns = [1] * len(matrix[0])

        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                if matrix[row][column] == 0:
                    rows[row] = 0
                    columns[column] = 0

        for row in range(len(matrix)):
            if rows[row] == 0:
                for column in range(len(matrix[row])):
                    matrix[row][column] = 0
            
        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                if columns[column] == 0:
                    matrix[row][column] = 0



        