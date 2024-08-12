class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        count=0
        for i in s:
            if i == '(':
                stack.append(i)
                count=max(count,len(stack))
            if i == ')':
                stack.pop()
                count=max(count,len(stack))
        return count
            
        