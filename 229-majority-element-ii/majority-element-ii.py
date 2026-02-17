import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        track = {}
        offset = math.floor(len(nums) / 3)
        ans = []

        for num in nums:
            track[num] = track.get(num, 0) + 1
        
        for num in track.keys():
            if track[num] > offset:
                ans.append(num)
        
        return ans