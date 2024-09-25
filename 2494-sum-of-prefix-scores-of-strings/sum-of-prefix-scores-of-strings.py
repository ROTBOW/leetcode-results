from collections import Counter

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        res = [0] * len(words)
        count = Counter()

        for word in words:
            for i in range(len(word)):
                count[word[:i+1]] += 1

        for idx, word in enumerate(words):
            for i in range(len(word)):
                res[idx] += count[word[:i+1]]

        return res
                