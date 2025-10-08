class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        curr = []
        def dfs(i):
            if len(curr) == k:
                res.append(curr.copy())
                return
            
            if i >= n + 1:
                return
            
            curr.append(i)
            dfs(i + 1)

            curr.pop()
            dfs(i + 1)
        
        dfs(1)
        return res
