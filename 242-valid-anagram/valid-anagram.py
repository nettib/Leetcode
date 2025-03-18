class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashmap = {}
        t_hashmap = {}
        for char in s:
            if char not in s_hashmap:
                s_hashmap[char] = 1
            else:
                s_hashmap[char]+=1
        for char in t:
            if char not in t_hashmap:
                t_hashmap[char] = 1
            else:
                t_hashmap[char]+=1
        if s_hashmap == t_hashmap:
            return True
        return False 