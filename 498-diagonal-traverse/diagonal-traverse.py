class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        track = defaultdict(list)

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                s = r + c
                track[s].append(mat[r][c])
        
        print(track)
        ans = []

        size = len(mat) + len(mat[0]) - 1
        flag = 1

        for s in range(size):
            if flag:
                ans.extend(track[s][::-1])
                flag = 0
            else:
                ans.extend(track[s])
                flag = 1
        
        return ans