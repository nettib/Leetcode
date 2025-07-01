class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        major = 0

        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        for num in count:
            if major == 0 or count[num] > count[major]:
                major = num
        
        return major