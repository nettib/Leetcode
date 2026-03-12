from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_q = deque([])
        max_q = deque([])

        longest = 0
        l = 0
        for r in range(len(nums)):
            while min_q and nums[r] < min_q[-1]:
                min_q.pop()
            min_q.append(nums[r])

            while max_q and nums[r] > max_q[-1]:
                max_q.pop()
            max_q.append(nums[r])

            while abs(max_q[0] - min_q[0]) > limit:
                if min_q[0] == nums[l]:
                    min_q.popleft()
                if max_q[0] == nums[l]:
                    max_q.popleft()
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest

