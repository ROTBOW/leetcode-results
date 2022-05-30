TITLE = 'BackSpace String Compare'
'''
time: BigO(n)
space: BigO(n)

Results:
    Runtime: 73 ms, faster than 5.24%
    Memory Usage: 13.7 MB, less than 98.56%
'''
class Solution:
    def clean_up(self, word: str) -> str:
        stack = []
        for char in word:
            if char == '#' and len(stack):
                stack.pop()
            elif char != '#':
                stack.append(char)
        return ''.join(stack)
        
    
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.clean_up(s) == self.clean_up(t)