class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = float("inf")
        left = 0
        current = blocks[left:k]
        for right in range(k, len(blocks)):
            a = current.count("W")
            ans = min(ans, a)
            left += 1
            current = blocks[left:right + 1]
        a = current.count("W")
        ans = min(ans, a)
        return ans



        