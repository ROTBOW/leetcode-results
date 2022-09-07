import re
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        copy = s
        while True:
            s = re.sub(part, '', s, 1)
            if s == copy:
                break
            copy = s
            
        return s