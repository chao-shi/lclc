# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals = sorted(intervals, key=lambda x:(x.start, x.end))
        end_boundary = intervals[0].end
        rm_cnt = 0

        for i in range(1, len(intervals)):
            if intervals[i].start < end_boundary:
                rm_cnt += 1
                end_boundary = min(end_boundary, intervals[i].end)
            else:
                end_boundary = intervals[i].end
            
        return rm_cnt
    
# Line 21 is important !!! Have the choice to keep the smaller end.
# Also sort by end is important
