class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l, r = 0, len(citations) - 1
        hindex = 0

        while l <= r:
            m = l + ((r - l) // 2)
            count = len(citations) - m
            if count >= citations[m]:
                hindex = max(hindex, citations[m])
                l = m + 1
            else:
                if count <= citations[m]:
                    hindex = max(hindex, count)
                r = m - 1
        
        
        return hindex


    