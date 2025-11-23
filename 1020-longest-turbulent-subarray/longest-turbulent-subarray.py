class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n == 1:
            return 1

        def flagSwitch(prev, curr):
            if prev > curr:
                return -1
            elif prev < curr:
                return 1
            return 0

        maxLen = 1  # At least one element
        l = 0
        flag = 0  # No flag initially

        for r in range(1, n):
            flagR = flagSwitch(arr[r - 1], arr[r])

            if flagR == 0:
                l = r  # Reset window when equal elements
            elif r == 1 or flag * flagR == -1:
                # turbulent continues
                maxLen = max(maxLen, r - l + 1)
            else:
                # same sign, start new window
                l = r - 1
                maxLen = max(maxLen, r - l + 1)

            flag = flagR  # Always update flag

        return maxLen


