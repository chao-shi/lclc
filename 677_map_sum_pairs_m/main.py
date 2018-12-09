class TrieNode(object):
    def __init__(self):
        # self.val = val
        self.nexts = {}
        self.isWord = False
        self.sum = 0

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Depth d match d length string
        # Depth 0 matches empty string
        self.root = TrieNode()

    def upsert(self, word, delta):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        p = self.root
        for ch in word:
            p.sum += delta
            p = p.nexts.setdefault(ch, TrieNode())
        # Don't forget last
        p.sum += delta
        p.isWord = True


    def get_sum(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        p = self.root
        for ch in prefix:
            p = p.nexts.get(ch, None)
            if not p:
                return 0
        return p.sum

    
class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()
        self.map = collections.defaultdict(int)

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        if key in self.map and self.map[key] == val:
            return

        delta = val - self.map[key]
        self.map[key] = val
        self.trie.upsert(key, delta)
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return self.trie.get_sum(prefix)
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)