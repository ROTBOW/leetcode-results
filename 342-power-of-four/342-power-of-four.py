from math import sqrt
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num-1) == 0 and 0b1010101010101010101010101010101 & num == num