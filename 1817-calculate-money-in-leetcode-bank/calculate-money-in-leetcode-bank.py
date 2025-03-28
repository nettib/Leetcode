class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7
        total = 28 * weeks + 7 * weeks * (weeks - 1) // 2
        total += days * (weeks + 1 + weeks + days) // 2
        return total