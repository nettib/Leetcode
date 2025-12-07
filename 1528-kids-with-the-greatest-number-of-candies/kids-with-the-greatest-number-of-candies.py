class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = 0
        ans = []

        # getting max value
        for i in range(len(candies)):
            max_candy = max(max_candy, candies[i])

        for i in range(len(candies)):
            kid_candy = candies[i] + extraCandies
            ans.append(kid_candy >= max_candy)

        return ans
        