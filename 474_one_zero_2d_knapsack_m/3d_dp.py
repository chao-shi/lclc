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
        
        # Careful here when one of i, j is zero
        mt = collections.defaultdict(int)
        
        for i in range(m+1):
            for j in range(n+1):
                for k in range(1, len(cands) + 1):
                    c0, c1 = cands[k - 1]
                    max_cnt = mt[(i, j, k-1)]
                    if c0 <= i and c1 <= j:
                        max_cnt = max(max_cnt, mt[(i-c0, j-c1, k-1)] + 1)
                    mt[(i, j, k)] = max_cnt
        
        return mt[(m, n, len(cands))]
                        
                    
# Recursion function
# A(i, j, k) = max of {
#                    A(i, j, k - 1) if k > 0;
#                    A(i-cands[k-1][0], j - cands[k-1][1], k-1) if i >= cands[k-1][0] and j >= cands[k-1][1]
#        }

# Therefore safe to iterate from 0, because anyway we are checking on line 20, so 
# case of [0, 0, ?] won't be out of range. No need to specially process.


# Important thing for this question is 
# WHAT IS BASE CASE
# 
# k = 0 !!!