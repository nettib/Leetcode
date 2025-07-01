class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        major = None
        for num in nums:
            if major == None or count[num] > count[major]:
                major = num

        return major