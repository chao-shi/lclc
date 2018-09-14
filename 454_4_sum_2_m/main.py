class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        cnt_cd = collections.defaultdict(int)
        for c in C:
            for d in D:
                cnt_cd[c+d] += 1
        
        cnt = 0
        
        for a in A:
            for b in B:
                cnt += cnt_cd[-a - b]
        return cnt