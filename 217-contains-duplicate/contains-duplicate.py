class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a={}
        p=False
        for i in nums:
            if i not  in a:
                a[i]=0
            else:
                p=True
        return p
        
        