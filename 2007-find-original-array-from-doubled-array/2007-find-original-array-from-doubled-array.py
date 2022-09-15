from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        count = Counter(changed)
        changed.sort()
        res = []
        for num in changed:
            if count[num] > 0:
                if num == 0:
                    if count[0] >= 2:
                        res.append(0)
                        count[0] -= 2
                elif num*2 in count and count[num*2] > 0:
                    res.append(num)
                    count[num*2] -= 1
                    count[num] -= 1
                    
        return res if len(res) == (len(changed)//2) else []