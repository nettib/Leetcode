class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        l = 0

        for r in range(len(arr)):
            if arr[r] % 2 == 0:
                l = r + 1
            
            if r - l + 1 == 3:
                return True
        
        return False

