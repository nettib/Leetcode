from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(src):
            stack = [src]
            visited = set([src])

            while stack:
                node = stack.pop()
                if node == destination:
                    return True
                for nei in graph[node]:
                    if nei in visited: continue
                    stack.append(nei)
                    visited.add(nei)
            return False
            
        return dfs(source)