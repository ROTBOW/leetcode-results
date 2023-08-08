from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)
        s1 = Counter(s1)
        
        while r <= len(s2):
            if s1 == Counter(s2[l:r]):
                return True
            l += 1
            r += 1
            
        return False


