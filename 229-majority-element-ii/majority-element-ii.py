class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        major = []
        for num in nums:
            if count[num] > len(nums) // 3 and num not in major:
                major.append(num)

        return major