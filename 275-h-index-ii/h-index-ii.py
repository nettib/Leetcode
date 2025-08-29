class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l, r = 1, len(citations)
        hindex = 0
        
        while l <= r:
            m = l + ((r - l) // 2)
            count = 0
            for citation in citations:
                if citation >= m:
                    count += 1
            if count >= m:
                hindex= max(hindex, m)
                l = m + 1
            else:
                r = m - 1
        
        return hindex
    