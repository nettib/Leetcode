from collections import deque
class RecentCounter:

    def __init__(self):
        self.q = deque([])

    def ping(self, t: int) -> int:
        while self.q and ((self.q[0] < t - 3000) or (self.q[0] > t)):
            self.q.popleft()
        self.q.append(t)
        return len(self.q)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)