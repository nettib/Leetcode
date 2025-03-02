class Solution:
    # def sortedSquares(self, nums: List[int]) -> List[int]:
    #     for index in range(len(nums)):
    #         nums[index] = nums[index]**2
    #     nums.sort()
    #     return nums
    #Bruteforce Solution
    # def sortedSquares(self, nums: List[int]) -> List[int]:
    #     l, r = 0, len(nums) - 1
    #     while l < r:
    #         firstSquare = nums[l] ** 2
    #         secondSquare = nums[r] ** 2
    #         if firstSquare > secondSquare:
    #             nums[l], nums[r] = nums[r], nums[l] ** 2
    #             l+=1
    #         r-=1
    #     return nums
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        result = []
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                result.append(nums[l]**2)
                l+=1
            else:
                result.append(nums[r]**2)
                r-=1
        result.reverse()
        return result

        