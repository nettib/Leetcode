class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        run_sum = [nums[0]]

        for i in range(1, len(nums)):
            run_sum.append(nums[i] + run_sum[i - 1])

        nums.append(-float("inf"))
        stack = []

        _max = 0
        for i, num in enumerate(nums):
            while stack and stack[-1][-1] > num:
                _min_idx, _min = stack.pop()
                l = stack[-1][0] if stack else -1
                r = i

                if l >= 0:
                    _sum = (run_sum[r - 1] - run_sum[l])
                else:
                    _sum = (run_sum[r - 1])
                _max = max(_max, _min * _sum)
            
            stack.append([i, num])
        
        return _max % (10**9 + 7)
                
