# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        firstBad = 0
        l, r = 1, n

        while l <= r:
            m = l + ((r - l) // 2)
            if isBadVersion(m):
                firstBad = m
                r = m - 1
            else:
                l = m + 1
        
        return firstBad