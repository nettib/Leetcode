class Solution:
    def countAsterisks(self, s: str) -> int:
        inside = False
        count = 0
        for c in s:
            if c == '|':
                inside = not inside
            elif c == '*' and not inside:
                count += 1
        return count