from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for c1, c2 in prerequisites:
            graph[c2].append(c1)
        
        color = [0] * numCourses
        # 0 - white, 1 - gray, 2 - black
        visited = set()
        def dfs(node):

            for nei in graph[node]:
                if nei in visited:
                    if color[nei] == 1:
                        return False
                    continue
                color[nei] = 1
                visited.add(nei)
                if not dfs(nei):
                    return False
                
            color[node] = 2
            return True
        
        for c in range(numCourses):
            color[c] = 1
            visited.add(c)
            if not dfs(c):
                return False
        
        return True



        