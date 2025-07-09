import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(math.sqrt(c))
        while l <= r:
            track_sum = l**2 + r**2
            if track_sum == c:
                return True
            elif track_sum < c:
                l += 1
            else:
                r -= 1
        
        return False
        