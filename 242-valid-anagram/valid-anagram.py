from collections import defaultdict as ddict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d = ddict(int)

        for i in range(len(s)):
            d[s[i]] += 1
            d[t[i]] -= 1
        
        for count in d.values():
            if count != 0:
                return False
                
        return True
        