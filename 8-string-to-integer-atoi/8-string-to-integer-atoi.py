import re
class Solution:
    def myAtoi(self, s: str) -> int:
        match = re.search(r'^\s*(?P<number>[-+]?\d+)', s)
        if not match:
            return 0
        number = int(match.group('number'))
        
        if 2147483648 <= number:
            return 2147483647
        elif -2147483648 >= number:
            return -2147483648
        return number
        