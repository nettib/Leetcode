class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # My Solution
        # res = [1]

        # for i in range(rowIndex):
        #     nums = res.copy()
        #     for j in range(1, len(nums)):
        #         nums[j] = res[j] + res[j - 1]
        #     nums.append(1)
        #     res = nums

        # return res

        res = [1]

        for i in range(rowIndex):
            nums = [0] * (len(res) + 1)
            for j in range(len(res)):
                nums[j] += res[j]
                nums[j + 1] += res[j]
            res = nums
        
        return res