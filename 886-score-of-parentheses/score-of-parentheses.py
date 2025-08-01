class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            else:
                current_score = 0
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    while stack and isinstance(stack[-1], int):
                        current_score += stack[-1]
                        stack.pop()
                    stack.pop()
                    stack.append(2 * current_score)
        
        return sum(stack)