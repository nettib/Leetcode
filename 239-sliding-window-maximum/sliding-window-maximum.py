class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        maxHolder = []
        q = deque([])

        for i in range(k):
            while q and q[-1] < nums[i]:
                q.pop() 
            q.append(nums[i])
        
        maxHolder.append(q[0])

        for i in range(k, len(nums)):
            if nums[i - k] == q[0]:
                q.popleft()
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
            maxHolder.append(q[0])
        
        return maxHolder
