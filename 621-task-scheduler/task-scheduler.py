from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks).values()
        max_count = max(counts)
        num_max = list(counts).count(max_count)
        return max(len(tasks), (max_count-1)*(n+1) + num_max)