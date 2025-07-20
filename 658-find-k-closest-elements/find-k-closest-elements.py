class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = k - 1
        for i in range(k, len(arr)):
            if abs(arr[i] - x) < abs(arr[l] - x):
                r = i
                while r - l + 1 > k:
                    l += 1
        
        return arr[l: r + 1]

        