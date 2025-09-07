import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minInt = float("inf")

        while l <= r:
            m = l + ((r - l) // 2)
            timeCount = 0

            for pile in piles:
                timeCount += math.ceil(pile / m)

            if timeCount <= h:
                minInt = min(minInt, m)
                r = m - 1
            else:
                l = m + 1

        return minInt