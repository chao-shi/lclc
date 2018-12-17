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

        fs = map(lambda x:-x, counter_rev.keys())
        heapq.heapify(fs)
        res = []

        while len(res) < k:
            f = - heapq.heappop(fs)
            res.extend(sorted(counter_rev[f]))
        return res[:k]