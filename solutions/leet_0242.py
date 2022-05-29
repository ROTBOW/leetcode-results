TITLE = 'Vaild Anagram'
'''
time: BigO(n)
space: BigO(n)

Results:
    Runtime: 55 ms, faster than 76.77%
    Memory Usage: 14.5 MB, less than 34.99% 
'''

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)