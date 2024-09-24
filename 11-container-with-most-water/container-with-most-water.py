class Solution:
    def maxArea(self, height: List[int]) -> int:
        # maxArea = 0
        # for i in range(len(height)):
        #     for j in range(len(height)):
        #         width = j-i
        #         length = min(height[i],height[j])
        #         area = width*length
        #         maxArea = max(maxArea,area)
        # return maxArea 
        maxarea = 0
        l=0
        r=len(height) - 1
        while l <= r:
            width = r - l
            length = min(height[l],height[r])
            area = width*length
            maxarea = max(maxarea,area)
            if height[l] < height[r]:
                l+=1
            elif height[l] > height[r]:
                r-=1
            else:
                if r - l > 1:
                    if height[l+1] > height[r-1]:
                        l+=1
                    elif height[l+1] < height[r-1]:
                        r-=1
                    else:
                        l+=1
                else:
                    break
        return maxarea
                    
