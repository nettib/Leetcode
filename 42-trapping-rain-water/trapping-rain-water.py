class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        water = 0

        while l < r:
            if maxL < maxR:
                l += 1
                water += max(maxL - height[l], 0)
                maxL = max(maxL, height[l])
            else:
                r -= 1
                water += max(maxR - height[r], 0)
                maxR = max(maxR, height[r])
        
        return water