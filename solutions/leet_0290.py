TITLE = 'word pattern'
'''
time: BigO(n)
space: BigO(n)

Results:
    Runtime: 43 ms, faster than 46.07%
    Memory Usage: 13.8 MB, less than 76.47%
'''
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(pattern) != len(words): return False
        coral, paired_words = dict(), set()
        for i in range(len(pattern)):
            if pattern[i] not in coral and words[i] not in paired_words:
                coral[pattern[i]] = words[i]
                paired_words.add(words[i])
            elif coral.get(pattern[i]) != words[i]:
                return False

        return True
                