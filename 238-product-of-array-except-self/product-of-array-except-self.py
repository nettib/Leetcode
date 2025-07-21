class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        prefix = [0] * len(nums)
        prefix[0] = nums[0]

        postfix = [0] * len(nums)
        postfix[len(nums) - 1] = nums[len(nums) - 1]

        for i in range(1, len(nums)):
            prefix[i] = nums[i] * prefix[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = nums[i] * postfix[i + 1]

        ans[0] = postfix[1]
        ans[len(nums) - 1] = prefix[len(nums) - 2]

        for i in range(1, len(nums) - 1):
            ans[i] = prefix[i - 1] * postfix[i + 1]
        
        return ans
        
       
