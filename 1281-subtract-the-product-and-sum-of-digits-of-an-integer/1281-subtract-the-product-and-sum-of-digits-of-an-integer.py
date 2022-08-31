class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(x) for x in str(n)]
        prod = 1
        for num in digits: prod *= num
        return prod - sum(digits)