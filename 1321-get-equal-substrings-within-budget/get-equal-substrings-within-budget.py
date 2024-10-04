class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        mx = 0
        cost = 0
        for right in range(len(s)):
            cost += abs(ord(s[right]) - ord(t[right]))
            while cost > maxCost:
                cost-=abs(ord(s[left]) - ord(t[left]))
                left+=1
            mx = max(mx,right - left + 1)
        return mx