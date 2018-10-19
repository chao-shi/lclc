class Solution(object):
    def wordsAbbreviation(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        TrieNode = lambda: (collections.defaultdict(TrieNode), collections.defaultdict(int))
        
        groups = collections.defaultdict(list)

        for i, w in enumerate(dict):
            groups[(len(w), w[0], w[-1])].append((i, w))

        res = [None] * len(dict)

        for group in groups.values():
            root = TrieNode()

            for _, word in group:
                p = root
                for i in xrange(len(word)):
                    ch = word[i]
                    abbr = word[i+1:] if i >= len(word) - 3 else str(len(word) - i - 2) + word[-1]
                    p = p[0].setdefault(ch, TrieNode())
                    p[1][abbr] += 1

            for ii, word in group:
                p = root
                i = 0
                while i < len(word):
                    abbr = word[i+1:] if i >= len(word) - 3 else str(len(word) - i - 2) + word[-1]
                    p = p[0][word[i]]
                    if p[1][abbr] == 1:
                        res[ii] = word[:i+1] + abbr
                        break
                    else:
                        i += 1
        return res        

# Has to remove all the function calls and use group to speedup.