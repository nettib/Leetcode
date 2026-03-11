class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][-1] < temp:
                last = stack.pop()
                ans[last[0]] = i - last[0]
            stack.append([i, temp])
        
        return ans

