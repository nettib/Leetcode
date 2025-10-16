class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []

        def dfs(idx):
            ans.append(path[:])
            if idx >= len(nums):
                return
            for i in range(idx, len(nums)):
                path.append(nums[i])
                dfs(i + 1)
                path.pop()
        
        dfs(0)
        return ans