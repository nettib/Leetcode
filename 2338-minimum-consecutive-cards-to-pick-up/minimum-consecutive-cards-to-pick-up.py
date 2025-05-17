class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        track = set()
        min_cards = float("inf")
        l = r = 0
        while l <= r and r < len(cards):
            if l == r or cards[r] not in track:
                track.add(cards[r])
                r += 1
            else:
                min_cards = min(min_cards, r - l + 1)
                track.remove(cards[l])
                l += 1
        if min_cards != float("inf"):
            return min_cards
        return -1
        
