class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []

        for char in tokens:
            val1 = 0
            val2 = 0
            if char not in operators:
                stack.append(char)
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(str(int(eval(val1 + char + val2))))
            
        return int(stack[-1])


