import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        major = []
        for num in count:
            if count[num] > math.floor(len(nums) / 3):
                major.append(num)

        return major