class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        track = defaultdict(list)

        rows = len(mat)
        cols = len(mat[0])

        for row in range(rows):
            for col in range(cols):
                track[row + col].append(mat[row][col])

        res = []
        count = 0
        for total in range(rows + cols):
            if count % 2:
                res += track[total]
            else:
                res += track[total][::-1]
            count += 1

        return res