class Solution:
    def isValid(self, s: str) -> bool:
        pair = { '(': ')', '{': '}', '[': ']' }
        stack = []

        for bracket in s:
            if bracket in pair:
                stack.append(bracket)
            elif len(stack) != 0 and bracket == pair[stack[len(stack) - 1]]:
                stack.pop()
            else:
                return False
            
        return len(stack) == 0
