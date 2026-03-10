class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                last, idx = stack.pop()
                temperatures[idx] = (i - idx)
            stack.append([temp, i])
        
        for temp, idx in stack:
            temperatures[idx] = 0
        
        return temperatures
