class TrieNode(object):
    def __init__(self):
        # self.val = val
        self.nexts = {}
        self.isWord = False
        self.idx = None

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Depth d match d length string
        # Depth 0 matches empty string
        self.root = TrieNode()

    def insert(self, word, idx):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        p = self.root
        for ch in word:
            p = p.nexts.setdefault(ch, TrieNode())
        p.isWord = True
        p.idx = idx
    
    # Find all prefix of input such that this prefix also exist in trie
    # For optimization, return list of len of prefixes + index
    def find_matching_prefixes(self, input):
        res = []
        p = self.root
        
        # To handle if "" in the given list
        if p.isWord:
            res.append((p.idx, 0))
        
        for i, ch in enumerate(input):
            p = p.nexts.get(ch, None)
            if not p:
                break
            if p.isWord:
                res.append((p.idx, i + 1))
        return res
            

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        trie_f, trie_r = Trie(), Trie()

        for i, w in enumerate(words):
            trie_f.insert(w, i)
            trie_r.insert(w[::-1], i)
            
        res = []
        # Try use part of i as palindrome
        for i, w in enumerate(words):
            # w is first segment (w_prefix + palin) + w_prefix_mirror
            for j, pre_len in trie_r.find_matching_prefixes(w):
                palin = w[pre_len:]
                if palin and palin[::-1] == palin:
                    res.append([i, j])
                elif not palin and i < j:
                    res.append([i, j])
                
            # w is second segment w_suffix_mirror + (palin + w_suffix) 
            for j, pre_len in trie_f.find_matching_prefixes(w[::-1]):
                palin = w[:len(w) - pre_len]
                if palin and palin[::-1] == palin:
                    res.append([j, i])
                elif not palin and i < j:
                    res.append([j, i])
                    
        return res
    
# Certain points
# In find_matching_prefixes, don't forget empty string prefix

# If palin is empty, we can calculate A, A_mirror and A_mirror, A twice
# This approach does not pass Memory usage, find_matching_prefixes is efficient 

# Better for long strings