import heapq
import itertools

# Min priority queue with upsert/delete supported (PirotityQueue)
# 
# v will be unique that's why we can use q_map here
# Python website following 
# https://docs.python.org/3/library/heapq.html
# Also uses a counter, because he needs to compare v
# In this question, we don't care about which v get popped first
# So we ignore counter.
# 
class PQ(object):

    def __init__(self):
        self.q = []
        self.q_map = {}


    def add(self, v, p):
        if v in self.q_map:
            self.remove(v)
        node = [p, v, True]
        heapq.heappush(self.q, node)
        self.q_map[v] = node


    def incr(self, v, p):
        p_base = 0
        if v in self.q_map:
            p_base =self.q_map[v][0]
        self.add(v, p_base + p)


    def remove(self, v):
        self.q_map.pop(v)[-1] = False


    def pop(self):
        while self.q:
            node = heapq.heappop(self.q)
            if node[-1]:
                del self.q_map[node[1]]
                return (node[0], node[1])
        return None


    def first(self):
        while self.q and not self.q[0][-1]:
            heapq.heappop(self.q)
        return self.q[0][:2] if self.q else None


    def size(self):
        return len(self.q_map)


class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        # directed graph edge from nodes before to nodes after
        in_map, out_map = {}, {}
        for seq in seqs:
            for i in range(len(seq)):
                in_map.setdefault(seq[i], set())
                out_map.setdefault(seq[i], set())
                if i > 0:
                    in_map[seq[i]].add(seq[i-1])
                if i < len(seq) - 1:
                    out_map[seq[i]].add(seq[i+1])

        pq = PQ()
        for k in in_map:
            pq.add(k, len(in_map[k]))

        uniq_seq = []

        while pq.size() > 0:

            cnt_0, k_0 = 0, None
            while pq.size() > 0:
                in_degree, v = pq.first()
                if in_degree == 0:
                    cnt_0 += 1
                    k_0 = v
                    pq.pop()
                else:
                    break

            if cnt_0 != 1:
                return False

            uniq_seq.append(k_0)

            for nei in out_map[k_0]:
                pq.incr(nei, -1)

        return uniq_seq == org
        
# Seems like by looking at all seqs, we should be able to deduce the only solution for
# The count of numbers in front of a specific element.
# And this solution should be 0, 1, 2, 3, ...
# 
# Some counter example are [1,2] [2, 3] [4] where 4 is free, we don't know how many in front of 4
# Also [1, 2], [2, 1]
# 

# Standard algorithm of how to find the total order by removing nodes.

