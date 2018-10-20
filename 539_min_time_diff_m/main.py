class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def toint(time):
            h, m = map(int, time.split(":"))
            return h * 60 + m
        
        tps = sorted(map(toint, timePoints))
        min_diff = tps[0] + 24 * 60 - tps[-1]
        for i in range(1, len(tps)):
            min_diff = min(min_diff, tps[i] - tps[i-1])
        return min_diff
    
# To improve to O(N), use set to remove duplicated timepoints, there can only be at most 1440 timepoints