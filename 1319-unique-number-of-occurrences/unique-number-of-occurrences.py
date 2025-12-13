class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        track = {}
        track_set = set()

        for i in range(len(arr)):
            track[arr[i]] = track.get(arr[i], 0) + 1
        
        for i in range(len(arr)):
            if track[arr[i]] == 0:
                continue
            elif track_set and track[arr[i]] in track_set:
                return False
            else:
                track_set.add(track[arr[i]])
                track[arr[i]] = 0
        
        return True