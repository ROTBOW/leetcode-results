from collections import defaultdict as ddict
class Solution: 
    def firstUniqChar(self, s: str) -> int:
        first_loca = ddict(lambda: [0, 0])
        for i in range(len(s)):
            char = s[i]
            if char not in first_loca:
                first_loca[char][0] = i
            first_loca[char][1] += 1
        res = float('inf')
        for k, v in first_loca.items():
            if v[1] == 1 and v[0] < res:
                    res = v[0]
        print(first_loca)
        return res if res != float('inf') else -1