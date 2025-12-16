from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.track = {}
        self.count_track = defaultdict(list)
        self.max_count = -float("inf")

    def push(self, val: int) -> None:
        self.track[val] = self.track.get(val, 0) + 1
        self.count_track[self.track[val]].append(val)
        self.max_count = max(self.max_count, self.track[val])

    def pop(self) -> int:
        value = self.count_track[self.max_count].pop()
        self.track[value] = self.track.get(value, 0) - 1
        if len(self.count_track[self.max_count]) == 0:
            self.max_count -= 1
        return value

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()