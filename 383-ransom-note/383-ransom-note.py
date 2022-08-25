from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = Counter(magazine)
        for letter in ransomNote:
            if letter in letters and letters[letter] > 0:
                letters[letter] -= 1
            else:
                return False
        
        return True