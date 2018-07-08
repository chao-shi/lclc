class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        wmap = {}
        for i, w in enumerate(words):
            wmap[w] = i

        res = []
        for i, w1 in enumerate(words):
            # len(w1) >= len(w2)
            # duplicated case when len(w1) == len(w2)
            
            for pre_len in range(len(w1) + 1):
                w2 = w1[:pre_len][::-1]
                palin = w1[pre_len:]
                if w2 in wmap and palin == palin[::-1]:
                    res.append((i, wmap[w2]))
                    
            for suf_len in range(len(w1) + 1):
                w2 = w1[len(w1) - suf_len:][::-1]
                palin = w1[:len(w1) - suf_len]
                if w2 in wmap and palin == palin[::-1]:
                    res.append((wmap[w2], i))
                    
        return [[i, j] for i, j in set(res) if i != j]

# Cleanest approach
# What to filter
# A A_mirror and A_mirror A counted twice
# Palindrome pair with itself

# Easier to filter at the end
# (Also doable by active filtering during loop, see trie solution)

# Less memory but less efficiency. The string prefix searching is slow
# Could be a serious issue for longer strings