class Solution:
    from collections import deque


    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # Compute prefix sums
        prefix_sums = [0]
        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)

        deq = deque()
        min_length = float('inf')

        for i in range(len(prefix_sums)):
            # Check if we found a valid subarray
            while deq and prefix_sums[i] - prefix_sums[deq[0]] >= k:
                min_length = min(min_length, i - deq.popleft())

            # Keep deque ordered to maintain shortest subarray potential
            while deq and prefix_sums[i] <= prefix_sums[deq[-1]]:
                deq.pop()

            # Add current index to deque
            deq.append(i)

        # Return the shortest length if found, else -1
        return min_length if min_length != float('inf') else -1
