TITLE = 'Find Center Of Star Graph'
'''
time: BigO(1)
space: BigO(1)

Results:
    Runtime: 1035 ms, faster than 72.09%
    Memory Usage: 49.9 MB, less than 39.83%
'''
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[1][0] in edges[0]:
            return edges[1][0]
        else:
            return edges[1][1]