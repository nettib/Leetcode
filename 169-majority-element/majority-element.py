class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        major = None

        for num in count:
            if major is None or (count[num] > count[major] and num != major):
                major = num

        return major