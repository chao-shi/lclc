class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        lb, hb = 0, len(citations)
        while lb <= hb:
            mid = (lb + hb) / 2
            if mid == 0 or citations[-mid] >= mid:
                # at least mid elements which are >= mid
                # Let's see if we can move mid up
                lb = mid + 1
            else:
                hb = mid - 1
        return hb

# Careful on line 10 when mid is in range [0, n]

# Last good version problem
# last value in [0, n] such that 
# at least v elements >= v