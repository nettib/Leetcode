from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # counting fresh oranges
        fresh_at_start = 0
        
        q = deque([])
        visited = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh_at_start += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
        
        # Do BFS and make fresh oranges rotten

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        
        m = 0
        fresh = 0
        flag = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr, nc) in visited: continue
                    visited.add((nr, nc))
                    if not inbound(nr, nc) or grid[nr][nc] == 0: continue
                    if grid[nr][nc] == 1:
                        flag = 1
                        fresh += 1
                        grid[nr][nc] = 2
                    q.append((nr, nc))
            if flag:
                m += 1
                flag = 0
        
        if fresh != fresh_at_start:
            return -1
        return m


