class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pos=0
        for num in nums:
            if num != val:
                nums[pos]=num
                pos+=1
        return pos