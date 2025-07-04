class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, columns = len(img), len(img[0])
        res = [[0] * columns for _ in range(rows)]

        for r in range(rows):
            for c in range(columns):
                total, cnt = 0, 0
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        if i < 0 or i == rows or j < 0 or j == columns:
                            continue
                        total += img[i][j]
                        cnt += 1
                res[r][c] = total // cnt

        return res