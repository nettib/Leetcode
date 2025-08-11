class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        res = [[1], [1, 1]]

        for i in range(numRows - 2):
            nums = res[-1].copy()
            for j in range(1, len(nums)):
                nums[j] = res[-1][j] + res[-1][j - 1]
            nums.append(1)
            res.append(nums)
        
        return res