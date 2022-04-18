TITLE = 'Zigzag conversion'
'''
time: BigO(n)
space: BigO(n)
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