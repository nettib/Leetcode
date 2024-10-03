class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def createDic(word):
            freq={}
            for char in word:
                if char in freq:
                    freq[char]+=1
                else:
                    freq[char]=1
            return freq
        p_freq = createDic(p)
        s_freq = {}
        res = []

        for i in range(len(s)):
            if s[i] in s_freq:
                s_freq[s[i]]+=1
            else:
                s_freq[s[i]]=1

            if i >= len(p):
                left = s[i-len(p)]
                if s_freq[left] == 1:
                    del s_freq[left]
                else:
                    s_freq[left]-=1

            if s_freq == p_freq:
                res.append(i - len(p) + 1)
        return res

        
        
        
        
        
        
        # @cache
        # def checkAnagram(word):
        #     if sorted(p) == sorted(word):
        #         return True
        #     return False
        # left = 0 
        # current = s[left:len(p)]
        # ans = []
        # for right in range(len(p),len(s)):
        #     if checkAnagram(current):
        #         ans.append(left)
        #     left+=1
        #     current = s[left:right+1]
        # if checkAnagram(current):
        #     ans.append(left)
        # return ans
