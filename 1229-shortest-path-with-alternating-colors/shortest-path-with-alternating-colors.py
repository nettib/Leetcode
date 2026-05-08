from collections import defaultdict, deque
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_adj = defaultdict(list)

        for u, v in redEdges:
            red_adj[u].append(v)
        
        blue_adj = defaultdict(list)

        for u, v in blueEdges:
            blue_adj[u].append(v)
        
        # red
        red_ans = [-1] * n
        q = deque([0])
        visited = set()
        visited.add((0, 'r'))
        l = 0
        flag = 'r'
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if red_ans[node] == -1:
                    red_ans[node] = l

                if flag == 'r':
                    for nei in red_adj[node]:
                        if (nei, 'r') in visited: continue
                        visited.add((nei, 'r'))
                        q.append(nei)
                elif flag == 'b':
                    for nei in blue_adj[node]:
                        if (nei, 'b') in visited: continue
                        visited.add((nei, 'b'))
                        q.append(nei)
            if flag == 'r':
                flag = 'b'
            else:
                flag = 'r'
            l += 1
        
        # blue
        blue_ans = [-1] * n
        q = deque([0])
        visited = set()
        visited.add((0, 'b'))
        l = 0
        flag = 'b'
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if blue_ans[node] == -1:
                    blue_ans[node] = l

                if flag == 'r':
                    for nei in red_adj[node]:
                        if (nei, 'r') in visited: continue
                        visited.add((nei, 'r'))
                        q.append(nei)
                elif flag == 'b':
                    for nei in blue_adj[node]:
                        if (nei, 'b') in visited: continue
                        visited.add((nei, 'b'))
                        q.append(nei)
            if flag == 'r':
                flag = 'b'
            else:
                flag = 'r'
            l += 1

        print("red_ans: ", red_ans)
        print("blue_ans: ", blue_ans)
        # final
        ans = [] 

        for i in range(n):
            if red_ans[i] == -1:
                _min = blue_ans[i]
            elif blue_ans[i] == -1:
                _min = red_ans[i]
            else:
                _min = min(red_ans[i], blue_ans[i])

            ans.append(_min)
        
        return ans
            


            
                
        