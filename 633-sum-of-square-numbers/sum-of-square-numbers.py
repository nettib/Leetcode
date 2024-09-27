class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a=0
        for num in range(0,c+1):
            if num**2 == c:
                return True
            elif num**2 > c:
                a=num
                break
        arr=list(range(0,a))
        l=0
        r=len(arr)-1
        while l<=r:
            if arr[l]**2 + arr[r]**2 == c:
                return True
            elif arr[l]**2 + arr[r]**2 > c:
                r-=1
            else:
                l+=1
        return False


        