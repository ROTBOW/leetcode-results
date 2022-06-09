TITLE = 'length of the last word'
'''
time: BigO(n)
space: BigO(1)

Results: 
    Runtime: 67 ms, faster than 5.60%
    Memory Usage: 13.8 MB, less than 78.62%
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        back = len(s)-1
        while s[back].isspace(): back -= 1
        
        count = 0
        while True:
            if back > -1 and not s[back].isspace():
                count += 1
                back -= 1
            else:
                break
        return count


        # one line solution
        # return len(s.strip().split(' ')[-1])