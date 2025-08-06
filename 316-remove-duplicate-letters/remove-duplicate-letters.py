class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        idxMap = {}
        track = set()
        stack = []

        for i, char in enumerate(s):
            idxMap[char] = i
        
        for i in range(len(s)):
            if not stack or (s[i] not in track and stack[-1] < s[i]):
                stack.append(s[i])
                track.add(s[i])
            while stack and s[i] not in track and stack[-1] > s[i] and idxMap[stack[-1]] > i:
                track.remove(stack[-1])
                stack.pop()

            if s[i] not in track:
                stack.append(s[i])
                track.add(s[i])
        
        return "".join(stack)
