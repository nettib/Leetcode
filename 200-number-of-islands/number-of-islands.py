class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        
        visited = set()
        def dfs(r, c):

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not inbound(nr, nc) or grid[nr][nc] == "0": continue
                if (nr, nc) in visited: continue
                visited.add((nr, nc))
                dfs(nr, nc)
        
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) in visited or grid[r][c] == "0": continue
                islands += 1
                visited.add((r, c))
                dfs(r, c)
        
        return islands 
