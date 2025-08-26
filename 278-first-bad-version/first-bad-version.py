# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        v1, v2 = 1, n
        while v1 < v2:
            vm = v1 + ((v2 - v1) // 2)
            if isBadVersion(vm):
                v2 = vm
            else:
                v1 = vm + 1

        return v1
