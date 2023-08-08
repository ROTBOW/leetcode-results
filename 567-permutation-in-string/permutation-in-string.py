class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        l, r = 0, len(s1)
        
        while r <= len(s2):
            if s1 == sorted(s2[l:r]):
                return True
            l += 1
            r += 1
        
        return False


