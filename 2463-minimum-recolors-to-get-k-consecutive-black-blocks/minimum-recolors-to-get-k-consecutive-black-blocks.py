class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minRecolor=float("inf")
        curr=""
        start=0
        for i in range(len(blocks)):
            curr+=blocks[i]
            if (i-start+1)==k:
                minRecolor=min(minRecolor,curr.count("W"))
                print(curr)
                curr=blocks[start+1:i+1]
                start+=1
        return minRecolor


        