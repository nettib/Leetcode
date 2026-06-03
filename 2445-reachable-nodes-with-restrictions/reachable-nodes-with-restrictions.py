class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)
        r = [0] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        for node in restricted:
            r[node] = 1

        
        q = deque([0])
        visited = {0}
        nodes = 1

        while q:
            node = q.popleft()

            for nei in graph[node]:
                if nei in visited: continue
                visited.add(nei)
                if r[nei]: continue
                nodes += 1
                q.append(nei)
        
        return nodes
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna