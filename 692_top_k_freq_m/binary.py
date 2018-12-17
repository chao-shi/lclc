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
        
        # Like last good version problem
        # Last frequency F such that count(f >= F) >= k
        # So we can pick from words with frequency F
        
        # the code below is still N * logN, because max(fs) can go close to N
        fs = counter_rev.keys()
        lb, hb = min(fs), max(fs)
        while lb <= hb:
            f = (lb + hb) / 2
            c = sum([1 for w in counter if counter[w] >= f])
            if c < k:
                # bad version
                hb = f - 1
            else:
                lb = f + 1
        
        F = hb
        cands = [(w, counter[w]) for w in counter if counter[w] >= F]
        cands = sorted(cands, key = lambda x:(-x[1], x[0]))
        cands = cands[:k]
        return map(lambda x:x[0], cands)
        
# Still N * logN