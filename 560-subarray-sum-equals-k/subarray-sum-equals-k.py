class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        track = {0: 1}
        ans = 0

        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        for i in range(len(nums)):
            if nums[i] - k in track:
                ans += track[nums[i] - k]
            track[nums[i]] = track.get(nums[i], 0) + 1
        
        return ans
