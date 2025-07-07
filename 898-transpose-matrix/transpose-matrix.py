class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        columns = len(matrix[0])

        tran = [[0] * rows for _ in range(columns)]

        for r in range(len(tran)):
            for c in range(len(tran[0])):
                tran[r][c] = matrix[c][r]

        return tran