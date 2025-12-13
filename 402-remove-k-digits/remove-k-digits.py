class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for i in range(len(num)):
            while stack and k != 0 and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])
        
        while k:
            stack.pop()
            k -= 1
        
        ans = ""

        for num in stack:
            if not ans and num == "0":
                continue
            ans += num
        return ans if ans else "0"