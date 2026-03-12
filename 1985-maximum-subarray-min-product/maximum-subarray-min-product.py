class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        run_sum = [0]

        for i in range(len(nums)):
            run_sum.append(nums[i] + run_sum[-1])

        nums.append(-float("inf"))
        stack = []

        _max = 0
        for i, num in enumerate(nums):
            while stack and stack[-1][-1] > num:
                _min_idx, _min = stack.pop()
                l = stack[-1][0] if stack else -1
                r = i

                _sum = (run_sum[r] - run_sum[l + 1])
                _max = max(_max, _min * _sum)
            
            stack.append([i, num])
        
        return _max % (10**9 + 7)
                
