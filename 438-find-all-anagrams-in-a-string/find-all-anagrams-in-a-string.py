class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        @cache
        def checkAnagram(word):
            if sorted(p) == sorted(word):
                return True
            return False
        left = 0 
        current = s[left:len(p)]
        ans = []
        for right in range(len(p),len(s)):
            if checkAnagram(current):
                ans.append(left)
            left+=1
            current = s[left:right+1]
        if checkAnagram(current):
            ans.append(left)
        return ans
