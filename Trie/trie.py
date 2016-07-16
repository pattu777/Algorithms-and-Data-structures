# A pure Python implementation of a Trie.

class Node(object):
    def __init__(self, is_end=False, prefix_count=0):
        self.is_end = is_end
        self.prefix_count = prefix_count
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        """Insert a word into a Trie."""
        if isinstance(word, str):
            raise TypeError

        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = Node()
            current = current.children[letter]
        current.is_end = True


    def search(self, word):
        """Search if a word is present in a Trie."""
        current = self.root
        for letter in word:
            if letter in current.children:
                current = current.children[letter]
            else:
                return False
        return True
