TITLE = 'Vaild Parentheses'
'''
time: BigO(n)
space: BigO(n)

Results:
    Runtime: 33 ms, faster than 81.57%
    Memory Usage: 13.9 MB, less than 24.60%
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack, brackets = [], {')':'(', '}': '{', ']': '['}
        heads = {'[', '(', '{'}
        for bracket in s:
            if bracket in heads:
                stack.append(bracket)
            else:
                if stack and stack[-1] == brackets[bracket]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0