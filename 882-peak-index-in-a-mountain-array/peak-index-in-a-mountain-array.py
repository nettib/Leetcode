class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if m > 0 and arr[m] < arr[m - 1]:
                r = m - 1
            elif m < len(arr) - 1 and arr[m] < arr[m + 1]:
                l = m + 1
            else:
                return m
