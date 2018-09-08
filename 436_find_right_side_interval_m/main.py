# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        # Treemap like structure
        start_map = {intv.start : i for i, intv in enumerate(intervals)}
        sorted_start = sorted(start_map.keys())
        
        res = []
        for intv in intervals:
            end = intv.end
            idx = bisect.bisect_left(sorted_start, end)
            if idx == len(sorted_start):
                res.append(-1)
            else:
                res.append(start_map[sorted_start[idx]])
        return res