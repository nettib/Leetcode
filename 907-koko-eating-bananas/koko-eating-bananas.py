import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = float("inf")

        l, r = 1, max(piles)
        while l <= r:
            m = l + ((r - l) // 2)
            hr = 0
            for pile in piles:
                hr += math.ceil(pile / m)
            if hr <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        
        return res