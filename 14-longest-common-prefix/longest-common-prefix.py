class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        word = strs[0]
        for i in range(len(word)):
            for j in range(1, len(strs)):
                if i < len(strs[j]):
                    if word[i] != strs[j][i]:
                        return ans
                else:
                    return ans
            ans += word[i]
        return ans