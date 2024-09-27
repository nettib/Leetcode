import math
class Solution:
  def judgeSquareSum(self, c: int) -> bool:
    l = 0
    r = int(math.sqrt(c))  
    while l <= r:
        current_sum = l**2 + r**2
        if current_sum == c:
            return True
        elif current_sum < c:
            l += 1
        else:
            r -= 1
    
    return False
        



        # a=0
        # for num in range(0,c+1):
        #     if num**2 == c:
        #         return True
        #     elif num**2 > c:
        #         a=num
        #         break
        # arr=list(range(0,a))
        # l=0
        # r=len(arr)-1
        # while l<=r:
        #     if arr[l]**2 + arr[r]**2 == c:
        #         return True
        #     elif arr[l]**2 + arr[r]**2 > c:
        #         r-=1
        #     else:
        #         l+=1
        # return False


        