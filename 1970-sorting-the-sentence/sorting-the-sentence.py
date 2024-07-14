class Solution:
    def sortSentence(self, s: str) -> str:
        r=""
        for j in range(1,len(s.split())+1):
            for i in s.split():
                if str(j) in i:
                    h=i.replace(str(j),"")
                    r=r+h+" "
        return r.strip()

        