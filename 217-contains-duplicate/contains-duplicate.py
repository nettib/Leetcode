class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        is_there = set()

        for num in nums:
            if num in is_there:
                return True
            is_there.add(num)

        return False