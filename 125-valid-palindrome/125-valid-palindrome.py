from string import ascii_letters
class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = {'z', 'E', 'c', 'x', 'S', 'A', 'C', 'B', 'r', 'H', 'v', 'P', 'L', 'V', 'W', 'j', 'y', 'g', 'I', 'Q', 'U', 'w', 'M', 't', 's', 'd', 'D', 'G', 'a', 'T', 'q', 'O', 'l', 'R', 'k', 'J', 'n', 'i', 'u', 'o', 'e', 'f', 'N', 'F', 'K', 'h', 'Z', 'b', 'Y', 'p', 'm', 'X', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

        new_str = ''
        for char in s:
            if char in letters:
                new_str += char.lower()
                
        return new_str == new_str[::-1]