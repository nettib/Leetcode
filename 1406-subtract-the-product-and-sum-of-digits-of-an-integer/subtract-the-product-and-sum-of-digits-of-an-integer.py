class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1 
        total = 0
        for num in str(n):
            product *= int(num)
            total += int(num)
        return product - total
