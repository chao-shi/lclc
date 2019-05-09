class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        n = len(org)
        
        # annoying pre-checking
        if any(e > n or e < 1 for seq in seqs for e in seq):
            return False
        if any(len(set(seq)) != len(seq) for seq in seqs):
            return False
        if len({e for seq in seqs for e in seq}) != n:
            return False

        # Easy to detect loop with the help of some sequence
        idxmap = {e:i for i, e in enumerate(org)}

        next = {i:set() for i in range(1, n+1)}
        for seq in seqs:
            for i in range(0, len(seq) - 1):
                # loop detection
                if idxmap[seq[i]] > idxmap[seq[i+1]]:
                    return False
                next[seq[i]].add(seq[i+1])
        
        for i in range(len(org) - 1):
            e1, e2 = org[i], org[i+1]
            if e2 not in next[e1]:
                return False
        return True

