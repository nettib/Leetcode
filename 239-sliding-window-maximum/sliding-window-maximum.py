from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q = deque([])
        ans = []
        l = 0

        for r in range(k):
            while q and q[-1] < nums[r]:
                q.pop()
            q.append(nums[r])

        ans.append(q[0])
        l += 1

        for r in range(k, len(nums)):
            if l != 0 and q[0] == nums[l - 1]:
                q.popleft()
            while q and q[-1] < nums[r]:
                q.pop()
            q.append(nums[r])  
            ans.append(q[0])
            # print((l, r))
            l += 1
        
        return ans
            