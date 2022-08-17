class Solution:
    
    def word_to_morse(self, word):
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = ''
        for letter in word: res += morse[ord(letter) - 97]
        return res
                

    
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = set()
        
        for word in words:
            codes.add(self.word_to_morse(word))
        
        return len(codes)