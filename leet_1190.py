TITLE = 'Reverse Substrings Between Each Pair of Parentheses'
'''
time: BigO(n)
space: Big0(n)
'''

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if len(stack) > 0:
                if char == ')':
                    parStart = len(stack) - stack[::-1].index('(') - 1
                    
                    stackEnd = stack[parStart:]
                    stackEnd.pop(0)
                    stack = stack[:parStart] + stackEnd[::-1]
                    
            if char != ')':
                stack.append(char)
            
            
        return ''.join(stack)