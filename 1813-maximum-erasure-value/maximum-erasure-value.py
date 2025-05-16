class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        mx_score = 0
        count = 0
        l = r = 0
        while l <= r and r < len(nums):
            if l == r:
                count += nums[r]
                mx_score = max(mx_score, count)
                r += 1
            else:
                if nums[r] not in nums[l:r]:
                    count += nums[r]
                    mx_score = max(mx_score, count)
                    r += 1
                else:
                    count -= nums[l]
                    mx_score = max(mx_score, count)
                    l += 1
        return mx_score


        