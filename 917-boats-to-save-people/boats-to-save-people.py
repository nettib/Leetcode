class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 1    5       0 3 
        #    lr          l r
        # [1,2,2,3]     [1,2]
        # 0      5
        # lr
        # [3,3,4,5]
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0
        while l <= r:
            weight = people[l] + people[r]
            if weight > limit:
                r -= 1
                boats += 1
            else:
                l += 1
                r -= 1
                boats += 1
        if l == r:
            boats += 1
        return boats

