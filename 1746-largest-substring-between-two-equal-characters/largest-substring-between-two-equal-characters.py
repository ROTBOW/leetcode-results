class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = dict()
        res = 0

        for i in range(len(s)):
            letter = s[i]
            if letter not in seen:
                seen[letter] = i
            else:
                seen['found'] = True
                res = max(res, i - seen[letter] - 1)

        return res if 'found' in seen else -1