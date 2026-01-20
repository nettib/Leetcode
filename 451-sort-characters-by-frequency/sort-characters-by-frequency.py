class Solution:
    def frequencySort(self, s: str) -> str:
        track = {}

        for char in s:
            track[char] = track.get(char, 0) + 1
        
        track1 = defaultdict(list)
        
        for char in track.keys():
            val = track[char]
            track1[val].append(char)
        
        # print(track1)
        
        ans = ""
        for freq in sorted(track1)[::-1]:
            for char in track1[freq]:
                ans += (char * freq)
        
        return ans
