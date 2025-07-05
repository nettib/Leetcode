class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        track = set()
        res = []
        for i in range(len(nums)):
            if nums[i] in track:
                res.append(nums[i])
            else:
                track.add(nums[i])

        return res