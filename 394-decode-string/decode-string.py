class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] == "]":
                temp = ""
                num = ""
                while stack and stack[-1] != "[":
                    temp = stack.pop() + temp
                stack.pop()
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num) * temp)
            else:
                stack.append(s[i])
        
        return "".join(stack)