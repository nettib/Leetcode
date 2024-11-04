class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        min_length = float("inf")
        if nums[l] >= target:
            return 1
        r = l + 1
        total = 0
        for r in range(len(nums)):
            total+=nums[r]
            while total >= target:
                min_length = min(min_length, r - l + 1)
                total-=nums[l]
                l+=1
        if min_length == float("inf"):
            return 0
        return min_length



        # l=0
        # res = float("inf")
        # current = 0
        # for r in range(len(nums)):
        #     current+=nums[r]
        #     while current >= target:
        #         res=min(res,r-l+1)
        #         current-=nums[l]
        #         l+=1
        # if res == float("inf"):
        #     return 0
        # return res
            
        
        
        # res=float("inf")
        # l=0
        # r=0
        # flag = False
        # while l <= r and r < len(nums):
        #     arr = nums[l:r + 1]
        #     current = sum(arr)
        #     if current >= target:
        #         res=min(res,len(arr))
        #         flag = True
        #         l+=1
        #     else:
        #         r+=1
        # if flag == True:
        #     return res
        # return 0



        # left = 0
        # currentSum = 0
        # minLength = float("inf")
        # for right in range(len(nums)):
        #     currentSum+=nums[right]
        #     while currentSum>= target:
        #         minLength = min(minLength,right-left+1)
        #         currentSum -=nums[left]
        #         left+=1
        # if minLength == float("inf"):
        #     return 0
        # else:
        #     return minLength

