class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        for i in range(len(s)):
            if s[i] in "([{":
                arr.append(s[i])
            else:
                if len(arr) != 0:
                    if s[i] == ')' and arr[-1] == "(":
                        arr.pop()
                    elif s[i] == "]" and arr[-1] == "[":
                        arr.pop()
                    elif s[i] == "}" and arr[-1] == "{":
                        arr.pop()
                    else:
                        arr.append(s[i])
                else:
                    arr.append(s[i])

        return len(arr) == 0

        # dic={')':'(',']':'[','}':'{'}
        # stack=[]
        # if s[0] in dic.keys():
        #     return False 
        # for char in s:
        #     if char in dic.values():
        #         stack.append(char)
        #     else:
        #         if len(stack)!=0:
        #             if dic[char]!=stack[-1]:
        #                 return False
        #             else:
        #                 stack.pop()
        #         else:
        #             if dic[char]:
        #                 if len(stack)==0:
        #                     return False
        # if len(stack)==0:
        #     return True
        # else:
        #     return False
        # print(stack)
        
        