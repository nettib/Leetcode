class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                word = ""
                num = ""

                while stack[-1] != '[':
                    word += stack[-1]
                    stack.pop()
                stack.pop()

                word = word[::-1]

                while stack and stack[-1].isdigit():
                    num += stack[-1]
                    stack.pop()
                
                num = num[::-1]
                
                stack += list(int(num) * word)

        
        return "".join(stack)


