from functools import lru_cache

class Solution:
    
    # @lru_cache
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n if n >= 0 else 0
        
        n1, n2 = 2, 1
        ans = 0
        
        for step in range(2, n):
            ans = n1 + n2
            n2 = n1
            n1 = ans
            
        return ans
        
        