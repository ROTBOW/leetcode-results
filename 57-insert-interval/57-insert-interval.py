class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        intervals = intervals[::-1]
        result = []
        
        while len(intervals) > 0:
            if newInterval and intervals[-1][1] >= newInterval[0]:
                intervals.append(newInterval)
                newInterval = None
                
            if len(intervals) > 1 and intervals[-1][1] >= intervals[-2][0]:
                old_inter = intervals.pop()
                intervals[-1][0] = min(intervals[-1][0], old_inter[0])
                intervals[-1][1] = max(intervals[-1][1], old_inter[1])
            else:
                result.append(intervals.pop())
            
        if newInterval and newInterval[0] >= result[-1][1]:
            result += [newInterval]
        elif newInterval:
            result = [newInterval] + result
            
        return result# + intervals