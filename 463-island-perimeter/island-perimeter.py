class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        # Get starting point or land
        start = None
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    start = [r, c]
                    break
            if start:
                break

          
        # dfs
        perimeter = 0
        visited = set()

        visited.add(tuple(start))
        
        def dfs(r, c):
            nonlocal perimeter
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not inbound(nr, nc) or grid[nr][nc] == 0:
                    perimeter += 1
                    continue
                if (nr, nc) in visited:
                    continue
                visited.add((nr, nc))
                dfs(nr, nc)

        dfs(*start)
        return perimeter
                
