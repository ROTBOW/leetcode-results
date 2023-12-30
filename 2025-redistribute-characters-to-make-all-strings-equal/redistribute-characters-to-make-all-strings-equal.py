from collections import Counter

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = Counter()

        for word in words:
            count += Counter(word)

        for k, v in count.items():
            if v % len(words) != 0:
                return False

        return True