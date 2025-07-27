class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * n

        for first, last, seat in bookings:
            ans[first - 1] += seat
            if last < len(ans):
                ans[last] -= seat
        

        for i in range(1, len(ans)):
            ans[i] += ans[i - 1]

        return ans