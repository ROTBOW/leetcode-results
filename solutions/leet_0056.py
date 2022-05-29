TITLE = 'Merge Intervals'
'''
time: BigO(n log n)
space: BigO(n)

Results:
    Runtime: 155 ms, faster than 82.92%
    Memory Usage: 18.1 MB, less than 84.41%
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(reverse=True) # O(n log n)
        answer = []
        
        while len(intervals) > 1:
            if intervals[-1][1] >= intervals[-2][0]:
                temp_interval = [intervals[-1][0], max(intervals[-2][1], intervals[-1][1])]
                intervals.pop()
                intervals.pop()
                intervals.append(temp_interval)
            else:
                answer.append(intervals.pop())
                
        return answer + intervals