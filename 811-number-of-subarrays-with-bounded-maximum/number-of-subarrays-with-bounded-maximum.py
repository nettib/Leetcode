class Solution(object):
    def numSubarrayBoundedMax(self, nums, left, right):
        """
        :type nums: List[int]
        :type left: int
        :type right: int
        :rtype: int
        """
        def count(bound):
            curr = 0
            total = 0

            for num in nums:
                if num <= bound:
                    curr += 1
                    total += curr
                else:
                    curr = 0
            
            return total 
        
        return count(right) - count(left - 1)