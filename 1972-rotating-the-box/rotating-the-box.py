class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        rows = len(boxGrid)
        cols = len(boxGrid[0])

        for i in range(rows):
            r = cols - 1
            for l in range(cols - 1, -1, -1):
                if boxGrid[i][l] == "*":
                    r = l - 1
                elif boxGrid[i][r] != ".":
                    r -= 1
                elif boxGrid[i][l] == "#":
                    boxGrid[i][r] = "#"
                    boxGrid[i][l] = "."
                    r -= 1
        
        rows1 = len(boxGrid[0])
        cols1 = len(boxGrid)

        boxGrid1 = [[0 for _ in range(cols1)] for _ in range(rows1)]

        for i in range(rows):
            for j in range(cols):
                boxGrid1[j][i] = boxGrid[i][j]
        
        for i in range(rows1):
            l, r = 0, cols1 - 1
            while l <= r:
                boxGrid1[i][l], boxGrid1[i][r] = boxGrid1[i][r], boxGrid1[i][l]
                l += 1
                r -= 1
        
        return boxGrid1
