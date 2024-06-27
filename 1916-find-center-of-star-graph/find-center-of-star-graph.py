from collections import Counter
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        points = Counter([*edges[0], *edges[1]])
        
        res = prev = 0
        for point, count in points.items():
            if count > prev:
                prev = count
                res = point
        
        return res



