class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                val = stack.pop()
                res[val[-1]] = i - val[-1]
            stack.append([temp, i])
        
        return res