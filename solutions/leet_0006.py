TITLE = 'Zigzag conversion'
'''
time: BigO(n)
space: BigO(n)

Results:
    Runtime: 60 ms, faster than 86.91%
    Memory Usage: 14 MB, less than 77.35%
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [''] * numRows
        step, pointer = 1, 0
        for char in s:
            rows[pointer] += char
            
            if pointer == len(rows)-1:
                step = -1
            elif pointer <= 0:
                step = 1
            
                
            pointer += step
        
        return ''.join(rows)