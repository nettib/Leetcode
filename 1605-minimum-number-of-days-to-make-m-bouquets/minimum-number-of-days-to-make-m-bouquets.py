class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        l, r = min(bloomDay), max(bloomDay)
        minDay = float("inf")

        while l <= r:
            mid = l + ((r - l) // 2)
            print(mid)
            bouqet = 0
            count = 0
            for bloom in bloomDay:
                if bloom <= mid:
                    count += 1
                else:
                    if count >= k:
                        bouqet += (count // k)
                    count = 0
            if count >= k:
                bouqet += (count // k)
            if bouqet >= m:
                minDay = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return minDay