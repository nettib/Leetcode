class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1
        
        def get_sort_key(x):
            return (freq[x], -x)
        
        sorted_nums = sorted(nums, key=get_sort_key)
    
        return sorted_nums