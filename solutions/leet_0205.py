TITLE = 'Isomorphic Strings'
'''
time: BigO(n)
space: BigO(n)

Results:
    Runtime: 45 ms, faster than 79.04%
    Memory Usage: 14.3 MB, less than 45.51%
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        pattern = dict()
        seen = set()
        for i in range(len(s)):
            if s[i] not in pattern and t[i] not in seen:
                pattern[s[i]] = t[i]
                seen.add(t[i])
            elif pattern.get(s[i]) != t[i]:
                return False
        return True