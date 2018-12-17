class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counter = collections.Counter(words)
        counter_rev = collections.defaultdict(set)
        for w in counter:
            counter_rev[counter[w]].add(w)

        fs = sorted(counter_rev.keys(), reverse=True)
        res = []
        i = 0
        while len(res) < k:
            res.extend(sorted(counter_rev[fs[i]]))
            i += 1
        return res[:k]

# instead of sorting on line 13, which is actually sqrt(N) * logN
# number of unique frequencies is sqrt(N)
# See heap.py to make it k * logN
# Total N + k * logN

# QUESTION WRONG, NOT N * logK