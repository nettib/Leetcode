class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        mx_vowel = count
        l = 0
        for r in range(k, len(s)):
            if s[r] in vowels:
                count += 1
            if s[l] in vowels:
                count -= 1
            l += 1
            mx_vowel = max(mx_vowel, count)
        return mx_vowel


        