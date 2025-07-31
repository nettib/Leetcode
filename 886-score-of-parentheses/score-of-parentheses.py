class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for char in s:
            if char == '(':
                stack.append(char)
            else:
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    current_score = 0
                    while stack and isinstance(stack[-1], int):
                        current_score += stack.pop()
                    
                    stack.pop()
                    stack.append(2 * current_score)
                
        return sum(stack)