class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] #(num, min)
        currMin = nums[0]

        for i in range(1, len(nums)):
            while stack and stack[-1][0] < nums[i]:
                stack.pop()
            
            if stack and nums[i] < stack[-1][0] and nums[i] > stack[-1][1]:
                return True
            
            stack.append([nums[i], currMin])
            currMin = min(currMin, nums[i])
        
        return False