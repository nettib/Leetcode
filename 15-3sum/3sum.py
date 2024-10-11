class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array first
        ans = []
        
        for i in range(len(nums) - 2):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                
                if s == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for the second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for the third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif s < 0:
                    left += 1
                else:
                    right -= 1
        
        return ans




        