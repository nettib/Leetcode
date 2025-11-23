class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        numsR = []
        mp = {}
        rg = [0, float("inf")]

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                numsR.append((nums[i][j], i))
        
        numsR.sort()

        l = 0
        for r in range(len(numsR)):
            mp[numsR[r][1]] = mp.get(numsR[r][1], 0) + 1

            while len(mp) == len(nums):
                if rg[1] - rg[0] > numsR[r][0] - numsR[l][0]:
                    rg[0] = numsR[l][0]
                    rg[1] = numsR[r][0]
                mp[numsR[l][1]] = mp.get(numsR[l][1], 0) - 1
                if mp[numsR[l][1]] == 0:
                    del mp[numsR[l][1]]
                l += 1
        
        return rg

