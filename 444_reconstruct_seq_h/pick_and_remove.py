class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        # directed graph edge from nodes before to nodes after
        in_map = {}
        for seq in seqs:
            for i in range(len(seq)):
                # Don't forget last element
                in_map.setdefault(seq[i], set())
                if i > 0:
                    in_map[seq[i]].add(seq[i-1])

        # Build the unique sequence
        uniq_seq = []
        while in_map:
            # Find k_0 which has zero in degree, i.e. first in permutation
            cnt_0, k_0= 0, None
            for k in in_map:
                if len(in_map[k]) == 0:
                    k_0 = k
                    cnt_0 += 1
            
            # Some element are free or there is a loop
            if cnt_0 != 1:
                return False
        
            del in_map[k_0]
            uniq_seq.append(k_0)

            # remove node k_0 and its edges
            for k in in_map:
                if k_0 in in_map[k]:
                    in_map[k].remove(k_0)
        return uniq_seq == org
        
# Seems like by looking at all seqs, we should be able to deduce the only solution for
# The count of numbers in front of a specific element.
# And this solution should be 0, 1, 2, 3, ...
# 
# Some counter example are [1,2] [2, 3] [4] where 4 is free, we don't know how many in front of 4
# Also [1, 2], [2, 1]
# 
# TLE for this solution.