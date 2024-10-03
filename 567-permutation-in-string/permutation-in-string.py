class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def createDic(word):
            freq = {}
            for char in word:
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1
            return freq

        s1_freq = createDic(s1)
        s2_freq = {}

        for right in range(len(s2)):
            if s2[right] in s2_freq:
                s2_freq[s2[right]]+=1
            else:
                s2_freq[s2[right]] = 1

            if right >= len(s1):
                left = s2[right-len(s1)]
                if s2_freq[left] == 1:
                    del s2_freq[left]
                else:
                    s2_freq[left] -= 1

            if s1_freq == s2_freq:
                return True
        return False


        # @cache
        # def checking(word):
        #     if sorted(word) == sorted(s1):
        #         return True
        # l=0
        # r=len(s1)
        # while r < len(s2):
        #     current = s2[l:r]
        #     print(current)
        #     if checking(current):
        #         return True 
        #         break
        #     l+=1
        #     r+=1
        # return False
            

        