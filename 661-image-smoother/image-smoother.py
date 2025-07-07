class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        columns = len(img[0])

        matrix = [[0] * columns for _ in range(rows)]

        for r in range(rows):
            for c in range(columns):
                total = 0
                count = 0
                for i in range(r - 1, r + 2):
                    if i < 0 or i >= rows:
                        continue
                    for j in range(c - 1, c + 2):
                        if j < 0 or j >= columns:
                            continue
                        total += img[i][j]
                        count += 1
                
                matrix[r][c] = total // count

        return matrix