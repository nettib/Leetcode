class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        track = set()
        for i in range(k):
            if blocks[i] == "W":
                track.add(i)
        count = len(track)

        for i in range(k, len(blocks)):
            if blocks[i - k] == "W":
                track.remove(i - k)
            if blocks[i] == "W":
                track.add(i)
            count = min(count, len(track))

        return count