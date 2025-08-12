class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]

        for i in range(rowIndex):
            nums = res.copy()
            for j in range(1, len(nums)):
                nums[j] = res[j] + res[j - 1]
            nums.append(1)
            res = nums

        return res