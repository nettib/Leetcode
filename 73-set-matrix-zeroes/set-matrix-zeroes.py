class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()
        zero_columns = set()

        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                if matrix[row][column] == 0:
                    zero_rows.add(row)
                    zero_columns.add(column)

        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                if row in zero_rows or column in zero_columns:
                    matrix[row][column] = 0