from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = Counter(nums)

        major = None
        for num in nums:
            if major == None or count[num] > count[major]:
                major = num

        return major