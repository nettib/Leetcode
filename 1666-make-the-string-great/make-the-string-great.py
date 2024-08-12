class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        for i in s:
            if len(stack)==0:
                stack.append(i)
            else:
                if i==i.lower():
                    if stack[-1] != i.upper():
                        stack.append(i)
                    else:
                        stack.pop()
                if i==i.upper():
                    if stack[-1] != i.lower():
                        stack.append(i)
                    else:
                        stack.pop()
        return ''.join(stack)