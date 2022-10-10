from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = list(Counter(s).values())
        my_one = False
        ans = 0
        
        while counts:
            if counts[-1] >= 2:
                counts[-1] -= 2
                ans += 2
            else:
                if not my_one and counts[-1] > 0:
                    my_one = True
                    ans += 1
                    counts[-1] -= 1
                    
                counts.pop()
        
        return ans