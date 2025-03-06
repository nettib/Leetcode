class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if freq[nums[j]] > freq[nums[j+1]]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                elif freq[nums[j]] == freq[nums[j+1]]:
                    if nums[j] < nums[j+1]:
                        nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums