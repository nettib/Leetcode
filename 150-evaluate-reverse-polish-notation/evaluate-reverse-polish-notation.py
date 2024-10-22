class Solution:
   def evalRPN(self, tokens: List[str]) -> int:
    stack = []
    for i in range(len(tokens)):
        if tokens[i] not in "+-*/":
            stack.append(int(tokens[i]))
        elif tokens[i] == "+":
            if len(stack) > 1:
                a = stack[-2] + stack[-1]
                del stack[len(stack) - 2:len(stack)]
                stack.append(int(a))
        elif tokens[i] == "-":
            if len(stack) > 1:
                a = stack[-2] - stack[-1]
                del stack[len(stack) - 2:len(stack)]
                stack.append(int(a))
        elif tokens[i] == "*":
            if len(stack) > 1:
                a = stack[-2] * stack[-1]
                del stack[len(stack) - 2:len(stack)]
                stack.append(int(a))
        else:
            if len(stack) > 1:
                a = stack[-2] / stack[-1]
                del stack[len(stack) - 2:len(stack)]
                stack.append(int(a))
    return stack[0]



    # stack = []
    # for i in range(len(tokens)):
    #     if tokens[i] in ['+', '-', '*', '/']:
    #         b = stack.pop()
    #         a = stack.pop()
    #         res = eval(f"{a}{tokens[i]}{b}")
    #         stack.append(int(res))
    #     else:
    #         stack.append(tokens[i])
    # return int(stack[0])


        