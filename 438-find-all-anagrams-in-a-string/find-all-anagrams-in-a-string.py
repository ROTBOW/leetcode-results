from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = list()
        letters = Counter(p)
        window = Counter()
        window_end = len(s)-1

        for i in range(len(s)-1, -1, -1):
            char = s[i]

            if window_end - i == len(p):
                window[s[window_end]] -= 1
                window_end -= 1

            window[char] += 1

            if window == letters:
                res.append(i)

        return res

            
        