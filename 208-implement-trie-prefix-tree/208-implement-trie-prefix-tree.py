class Node:
    def __init__(self, val, is_word = False):
        self.val = val
        self.children = dict()
        self.is_word = is_word

class Trie:

    def __init__(self):
        self.root = Node(None)
        

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Node(letter)
                node = node.children[letter]
            else:
                node = node.children[letter]
        node.is_word = True
                

    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for letter in prefix:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)