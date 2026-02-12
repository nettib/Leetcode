class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        res = [[0] * len(img[0]) for _ in range(len(img))]

        def checkrow(row):
            if row >= 0 and row < len(img):
                return True
            return False
        
        def checkcol(col):
            if col >= 0 and col < len(img[0]):
                return True
            return False

        for r in range(len(img)):
            for c in range(len(img[0])):
                total = 0
                count = 0
                for i in range(r  - 1, r + 2):
                    if checkrow(i):
                        for j in range(c - 1, c + 2):
                            if checkcol(j):
                                total += img[i][j]
                                count += 1
            
                res[r][c] = total // count
        
        return res



