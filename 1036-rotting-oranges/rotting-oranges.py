from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        
        rotten = []

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    rotten.append([r, c])
        
        q = deque(rotten)
        m = 0
        while q:
            count = 0
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not inbound(nr, nc): continue
                    if grid[nr][nc] == 1:
                        count += 1
                        q.append([nr, nc])
                        grid[nr][nc] = 2
            if count:
                m += 1
         
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
        
        return m
            