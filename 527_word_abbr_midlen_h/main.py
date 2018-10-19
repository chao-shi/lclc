class TrieNode(object):
    # look_ahead contains the abbr including the char which bring to this node.
    def __init__(self):
        self.nexts = collections.defaultdict(TrieNode)
        self.look_ahead = collections.defaultdict(int)
    
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
    
    def insert(self, word):
        p = self.root
        # We can skip look_ahead map for root, since pattern like 8e is not allowed.
        for i, ch in enumerate(word):
            abbr = self.abbr(word, i)
            p = p.nexts.setdefault(ch, TrieNode())
            p.look_ahead[abbr] += 1
            
    
    def search_abbr(self, word):
        p = self.root
        i = 0
        while i < len(word):
            abbr = self.abbr(word, i)
            p = p.nexts[word[i]]
            if p.look_ahead[abbr] == 1:
                return word[:i+1] + abbr
            else:
                i += 1
    
    # calculate abbr starting with i+1
    def abbr(self, word, i):
        if i >= len(word) - 3:
            abbr = word[i+1:]
        else:
            abbr = str(len(word) - i - 2) + word[-1]
        return abbr

    
class Solution(object):
    def wordsAbbreviation(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        # Good that string are non-empty
        trie = Trie()
        for w in dict:
            trie.insert(w)
        return [trie.search_abbr(w) for w in dict]
        
        
# TLE
# OJ has problem, this should be the best solution