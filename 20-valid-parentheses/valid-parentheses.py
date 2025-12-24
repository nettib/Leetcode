class Solution:
    def isValid(self, s: str) -> bool:
        char_match = { ')': '(', '}': '{', ']': '[' }
        stack = []

        for char in s:
            if char not in char_match:
                stack.append(char)
            else:
                if not stack:
                    return False
                sign = stack.pop()
                if sign != char_match[char]:
                    return False
            
        return True if not stack else False