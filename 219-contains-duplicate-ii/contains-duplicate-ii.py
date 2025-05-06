class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        track = {}
        for i in range(len(nums)):
            if nums[i] in track and abs(i - track[nums[i]]) <= k:
                return True
            track[nums[i]] = i
        return False