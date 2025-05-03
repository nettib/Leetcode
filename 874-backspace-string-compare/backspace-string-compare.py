class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        t1 = []
        for i in range(len(s)):
            if s[i] == "#" and len(s1) != 0:
                s1.pop()
            elif s[i] != "#":
                s1.append(s[i])
        for i in range(len(t)):
            if t[i] == "#" and len(t1) != 0:
                t1.pop()
            elif t[i] != "#":
                t1.append(t[i])
        
        return s1 == t1