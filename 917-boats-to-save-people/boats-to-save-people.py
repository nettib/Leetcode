class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat = 0
        l, r = 0, len(people) - 1
        while l <= r:
            if l == r:
                boat += 1
                return boat
            weight = people[l] + people[r]
            if weight <= limit:
                boat += 1
                l += 1
                r -= 1
            else:
                boat += 1
                r -= 1
        
        return boat