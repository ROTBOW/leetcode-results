TITLE = 'search a 2D matrix'
'''
time: BigO(n)
space: BigO(1)

Results:
    Runtime: 49 ms, faster than 78.22%
    Memory Usage: 14.4 MB, less than 42.32%
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 1:
            if target in matrix[0]:
                return True
            else:
                return False
        
        
        for i in range(1, len(matrix)):
            if target >= matrix[i-1][0] and target < matrix[i][0]:
                return target in matrix[i-1]

        return target in matrix[-1]