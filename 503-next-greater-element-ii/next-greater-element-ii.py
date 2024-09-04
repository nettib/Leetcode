class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0, len(nums)):
            flag = 0
            if i == len(nums) -1:j = 0
            else:j = i + 1
            while j != i:
                if nums[j] > nums[i]:
                    ans.append(nums[j])
                    flag = 1
                    break
                if j == len(nums) - 1:
                    j = 0
                else:
                    j += 1
            if flag == 0:
                ans.append(-1)
        return ans