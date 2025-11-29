class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxEle = max(nums)
        cnt = 0
        ans = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == maxEle:
                cnt += 1
            
            while cnt > k or (cnt == k and nums[l] != maxEle):
                if nums[l] == maxEle:
                    cnt -= 1
                
                l += 1
            
            if cnt == k:
                ans += l + 1
            
        
        return ans
            
            


