class Solution:
   def evalRPN(self, tokens: List[str]) -> int:
    stack = []
    for i in range(len(tokens)):
        if tokens[i] in ['+', '-', '*', '/']:
            b = stack.pop()
            a = stack.pop()
            res = eval(f"{a}{tokens[i]}{b}")
            stack.append(int(res))
        else:
            stack.append(tokens[i])
    return int(stack[0])


        