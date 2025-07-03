class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}

        for char in s:
            if char not in count:
                count[char] = 0
            count[char] += 1

        long_palindrome = 0
        flag = 0

        for char in count:
            if (count[char] % 2 != 0 ) and (flag == 0) and (count[char] - count[char] % 2):
                long_palindrome += count[char] - (count[char] % 2)
                long_palindrome += 1
                flag = 1
            elif count[char] - count[char] % 2:
                long_palindrome += count[char] - (count[char] % 2)
            elif count[char] == 1 and flag == 0:
                long_palindrome += count[char]
                flag = 1
            

        return long_palindrome  