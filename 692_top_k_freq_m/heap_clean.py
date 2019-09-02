class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counters = collections.Counter(words)
        counters = [(-counters[w], w) for w in counters]
        heapq.heapify(counters)
        
        res = []
        while counters and len(res) < k:
            _, w = heapq.heappop(counters)
            res.append(w)
        return res