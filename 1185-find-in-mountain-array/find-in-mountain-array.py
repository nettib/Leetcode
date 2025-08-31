# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        peakIndex = -1
        l, r = 0, mountainArr.length() - 1

        while l <= r:
            m = l + ((r - l) // 2)
            if m > 0 and mountainArr.get(m) < mountainArr.get(m - 1):
                r = m - 1
            elif m < mountainArr.length() and mountainArr.get(m) < mountainArr.get(m + 1):
                l = m + 1
            else:
                peakIndex = m
                break

        
        l, r = 0, peakIndex

        while l <= r:
            m = l + ((r - l) // 2)
            if mountainArr.get(m) == target:
                return m
            elif mountainArr.get(m) < target:
                l = m + 1
            else:
                r = m - 1
        
        l, r = peakIndex, mountainArr.length() - 1

        while l <= r:
            m = l + ((r - l) // 2)
            if mountainArr.get(m) == target:
                return m
            elif mountainArr.get(m) < target:
                r = m - 1
            else:
                l = m + 1
        
        return -1