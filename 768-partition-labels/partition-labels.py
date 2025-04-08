class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        last = {}
        for i in range(len(s)):
                last[s[i]] = i
        track = {}
        l = r = 0
        while r < len(s):
            if l == r and last[s[l]] == l:
                res.append(r - l + 1)
                l += 1
                r += 1
            else:
                track[s[r]] = r
                if last[s[r]] == r:
                    del track[s[r]]
                if len(track) == 0:
                    res.append(r - l + 1)
                    l = r + 1
                r += 1
                # print(track)
        return res

