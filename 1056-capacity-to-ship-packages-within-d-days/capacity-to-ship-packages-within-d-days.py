import math
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        res = float("inf")
        l, r = max(weights), sum(weights)

        while l <= r:
            m = l + ((r - l) // 2)
            day = 1
            sumWeight = 0
            for weight in weights:
                sumWeight += weight
                if sumWeight > m:
                    day += 1
                    sumWeight = weight
            if day <= days:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1

        return res 
