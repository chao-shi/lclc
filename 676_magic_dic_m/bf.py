class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.dictionary = set(dict)
        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for i in range(len(word)):
            for ch_idx in range(26):
                ch = chr(ord('a') + ch_idx)
                if ch != word[i]:
                    replace_word = word[:i] + ch + word[i+1:]
                    if replace_word in self.dictionary:
                        return True
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)

# Prefix tree suboptimal to solve the problem because we need exact match. 
# Prefix tree still need to try to replace each character and then do the search down the root
# until find the exact match. Slower than hashkey based set approach