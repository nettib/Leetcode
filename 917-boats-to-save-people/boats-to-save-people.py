class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort() #O(nlog(n))

        l, r = 0, len(people) - 1
        boats = 0

        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            boats += 1
            r -= 1

        return boats + 1 if l == r else boats