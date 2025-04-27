class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            else:
                l, r = i + 1, len(nums) - 1
                while l < r:
                    total = nums[i] + nums[l] + nums[r]
                    if total < 0:
                        l += 1
                    elif total > 0:
                        r -= 1
                    else:
                        ans.append([nums[i], nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
        return ans

