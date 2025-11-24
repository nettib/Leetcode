class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        def flagSwitch(prev, curr):
            if prev < curr:
                return 1
            elif prev > curr:
                return -1
            return 0

        maxLen = 1
        l = 0
        flag = None

        for r in range(1, len(arr)):
            flagR = flagSwitch(arr[r - 1], arr[r])
            if flagR == 0:
                l = r
                flag = None
            if (flag and flagR == flag):
                l = r - 1
            maxLen = max(maxLen, r - l + 1)
            flag = flagR

        return maxLen