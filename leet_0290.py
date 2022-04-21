TITLE = 'word pattern'
'''
time: BigO(n)
space: BigO(n)
'''
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(pattern) != len(words): return False
        coral = dict()
        for pat, word in zip(pattern, words):
            if pat not in coral and word not in coral.values():
                coral[pat] = word
            else:
                try:
                    if coral[pat] != word:
                        return False
                except:
                    return False
        return True
                