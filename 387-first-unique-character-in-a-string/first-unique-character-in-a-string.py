class Solution:
    def firstUniqChar(self, s: str) -> int:
        count={}
        for index in range(len(s)):
            if s[index] not in count:
                count[s[index]]=[1,index]
            else:
                count[s[index]][0]+=1
        for k in count.keys():
            if count[k][0]==1:
                return count[k][1]
        return -1