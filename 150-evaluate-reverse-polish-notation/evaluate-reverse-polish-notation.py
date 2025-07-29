import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []

        for char in tokens:
            val1 = 0
            val2 = 0
            if char not in operators:
                stack.append(int(char))
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                print(str(val1) + char + str(val2))
                stack.append(math.trunc(eval(str(val1) + char + str(val2))))
            
        return stack[-1]


