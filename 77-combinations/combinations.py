class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(num):
            if len(path) == k:
                ans.append(path[:])
                return

            for i in range(num, n + 1):
                path.append(i)
                dfs(i + 1)
                path.pop()
            
        dfs(1)
        return ans