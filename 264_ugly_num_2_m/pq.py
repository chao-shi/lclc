import Queue
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        pq = Queue.PriorityQueue()
        pq.put(1)
        res = set()
        while len(res) < n:
            top = pq.get()
            for factor in [2, 3, 5]:
                pq.put(factor * top)
            res.add(top)
        return max(res)

# Timeout