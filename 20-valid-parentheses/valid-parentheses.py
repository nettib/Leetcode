class Solution:
    def isValid(self, s: str) -> bool:
        dic={')':'(',']':'[','}':'{'}
        stack=[]
        if s[0] in dic.keys():
            return False 
        for char in s:
            if char in dic.values():
                stack.append(char)
            else:
                if len(stack)!=0:
                    if dic[char]!=stack[-1]:
                        return False
                    else:
                        stack.pop()
                else:
                    if dic[char]:
                        if len(stack)==0:
                            return False
        if len(stack)==0:
            return True
        else:
            return False
        print(stack)
        
        