class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        track = set()

        for i in range(len(ranges)):
            for num in range(ranges[i][0], ranges[i][1] + 1):
                track.add(num)

        print(track) 
        for num in range(left, right + 1):
            if num not in track:
                return False
        
        return True
