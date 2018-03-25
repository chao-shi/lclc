class TrieNode(object):
    def __init__(self):
        # self.val = val
        self.nexts = {}
        self.isWord = False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Depth d match d length string
        # Depth 0 matches empty string
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        p = self.root
        for ch in word:
            p = p.nexts.setdefault(ch, TrieNode())
        p.isWord = True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p = self.root
        for ch in word:
            p = p.nexts.get(ch, None)
            if not p:
                return False
        return p.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        p = self.root
        for ch in prefix:
            p = p.nexts.get(ch, None)
            if not p:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# TrieNode val is handy but not necessary
# Shortest answer, good usage of setdefault