class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        pq = [1]
        res = set()
        while len(res) < n:
            top = heapq.heappop(pq)
            for factor in [2, 3, 5]:
                heapq.heappush(pq, factor * top)
            res.add(top)
        return max(res)

# Still TLE on OJ