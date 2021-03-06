class TrieNode(object):
    def __init__(self):
        # self.val = val
        self.nexts = {}
        self.isWord = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        p = self.root
        for ch in word:
            p = p.nexts.setdefault(ch, TrieNode())
        p.isWord = True


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.searchHelper(self.root, word)
        
    # Recursion needed
    def searchHelper(self, cur, word):
        if not word:
            return cur.isWord
        
        if word[0] == ".":
            for next in cur.nexts.values():
                if self.searchHelper(next, word[1:]):
                    return True
            return False
        elif word[0] in cur.nexts:
            return self.searchHelper(cur.nexts[word[0]], word[1:])
        else:
            return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)