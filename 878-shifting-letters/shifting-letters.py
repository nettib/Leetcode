class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        s1=""
        shifts=shifts[::-1]
        for i in range(1,len(shifts)):
            shifts[i]+=shifts[i-1]
        shifts=shifts[::-1]
        for i in range(len(s)):
            num=ord(s[i])+shifts[i]
            if num > ord('z'):
                num = (num - ord('a')) % 26 + ord('a')

            s1+=chr(num)
        return s1
           
