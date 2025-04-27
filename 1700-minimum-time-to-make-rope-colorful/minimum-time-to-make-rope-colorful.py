class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        min_time = 0
        l = 0
        for r in range(1, len(colors)):
            if colors[l] == colors[r]:
                min_time += min(neededTime[l], neededTime[r])
                if min(neededTime[l], neededTime[r]) == neededTime[r]:
                    neededTime[r] = neededTime[l]
            l += 1
        return min_time
