class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # array
        # push onto it checking if we hit our ch
        # if we do, reverse the array
        # return the array + whatever is left from the word
        arr = list()

        for idx, letter in enumerate(word):
            arr.append(letter)
            if letter == ch:
                arr = arr[::-1]
                return ''.join(arr) + word[idx+1:]

        return ''.join(arr)

            