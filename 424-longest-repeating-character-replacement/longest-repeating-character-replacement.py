class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_count = defaultdict(int)
        longest = 0

        l = 0
        for r in range(len(s)):
            s_count[s[r]] += 1
            
            while (sum(s_count.values()) - max(s_count.values())) > k:
                s_count[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)
        
        return longest