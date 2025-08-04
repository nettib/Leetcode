class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        track = {}
        max_fruit = 0

        l = 0
        for r in range(len(fruits)):
            track[fruits[r]] = track.get(fruits[r], 0) + 1

            while len(track) > 2:
                track[fruits[l]] -= 1
                if track[fruits[l]] == 0:
                    del track[fruits[l]]
                l += 1
            
            max_fruit = max(max_fruit, r - l + 1)
        
        return max_fruit
