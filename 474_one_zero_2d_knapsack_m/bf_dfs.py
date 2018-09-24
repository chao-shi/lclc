class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        cands = [(s.count("0"), s.count("1")) for s in strs]
        cands = [c for c in cands if c[0] <= m and c[1] <= n]
        
        # Trivial to solve here if one dimension
        # given array A and N, find max subset of array such that subset sum is smaller than N
        # (Note that this is a special case of 0-1 knapsack where price is always 1)
        
        # 1 Dimensional can always be solved by sorting, and choosing the smaller ones
        # 
        # Does a greedy approach exist for 2-d
        # Let's say we have (3, 4) and (4, 3), we cannot make the decision locally, because we 
        # don't know after this will 1 or 0 be more scarce?
        #
        # Answer is No, let's still use DFS
        
        self.max_set_size = 0
        def recur(i, set_size, r0, r1):
            # print i, set_size, r0, r1
            if i == len(cands):
                self.max_set_size = max(self.max_set_size, set_size)
                return 
            elif cands[i][0] <= r0 and cands[i][1] <= r1:
                recur(i + 1, set_size + 1, r0 - cands[i][0], r1 - cands[i][1])
            recur(i + 1, set_size, r0, r1)
            
        recur(0, 0, m, n)
        return self.max_set_size