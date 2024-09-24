class Solution:
    def reverseParentheses(self, s: str) -> str:
        # use a stack
        # add all char including (
        # when we hit a closer, then pop off the stack until we hit a opener
        # and then reappend whatever we've popped off to the stack
        # when we've gone through the whole thing, return the stack as a string
        stack = list() # time(n2) space(n)

        for char in s:
            if char != ")":
                stack.append(char)
            else:
                temp_stack = list()
                item = stack.pop()
                while item != '(':
                    temp_stack.append(item)
                    item = stack.pop()
                stack += temp_stack
        
        return ''.join(stack)