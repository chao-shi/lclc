class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def get_wildcards(self, w):
        wcs = []
        for i in range(len(w)):
            wcs.append(w[:i] + "*" + w[i+1:])
        return wcs
    
    
    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.all_words = set(dict)
        self.wc_dict = collections.defaultdict(int)
        for w in dict:
            for wc in self.get_wildcards(w):
                self.wc_dict[wc] += 1
        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for wc in self.get_wildcards(word):
            # Don't forget word not in self.all_words
            if wc in self.wc_dict and (self.wc_dict[wc] > 1 or word not in self.all_words) :
                return True
        return False
        
# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)

# Compared to BF, it saves the constant factor of 26
# Corner case. wc of the search word in the wc_dict, but only one word in dictionary contribute to the wc and 
# that word in the dictionary is same as word for search. Should return False 