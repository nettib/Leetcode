class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []
        res = []
        n = len(nums) / 2
        for i in range(len(nums)):
            if nums[i] < 0:
                negatives.append(nums[i])
            else:
                positives.append(nums[i])
        l = r = 0
        while l < n and r < n:
            if l == r:
                res.append(positives[l])
                l += 1
            else:
                res.append(negatives[r])
                r += 1
        res.append(negatives[r])
        return res

        