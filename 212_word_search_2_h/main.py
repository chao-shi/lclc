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

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board:
            return []

        m, n = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)
        res = set()
        visited = set()

        def recur(i, j, trie_node, word):
            if trie_node.isWord:
                res.add(word)
            
            visited.add((i, j))
            
            if i == None and j == None:
                next_coords = [(ti, tj) for ti in range(m) for tj in range(n)]
            else:
                next_coords = [(i + v[0], j + v[1]) for v in [(0, 1), (1, 0), (0, -1), (-1, 0)]]
            
            for ii, jj in next_coords:
                if 0 <= ii < m and 0 <= jj < n and (ii, jj) not in visited:
                    ch = board[ii][jj]
                    if ch in trie_node.nexts:
                        recur(ii, jj, trie_node.nexts[ch], word + ch)
            
            visited.remove((i, j))
        
        recur(None, None, trie.root, "")
        return list(res)
    
# Trick, start recursion of i, j, make it both None and trie_node is None
# Don't forget visited set

# 760ms beats 32%