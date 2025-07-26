class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        track = {0}
        count = 0

        prefix = 0
        for num in nums:
            prefix += num
            if prefix - target in track:
                count += 1
                prefix = 0
                track = {0}
            else:
                track.add(prefix)

        return count
