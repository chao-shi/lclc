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
        
        start_idx = sorted([(v[0], i) for i, v in enumerate(intervals)])
        end_idx = sorted([(v[1], i) for i, v in enumerate(intervals)])

        j = len(intervals) - 1

        res = [None] * len(intervals)

        for i in range(len(intervals) - 1, -1, -1):
            while start_idx[j][0] >= end_idx[i][0]:
                j -= 1
            if j + 1 == len(intervals):
                res[end_idx[i][1]] = -1
            else:
                res[end_idx[i][1]] = start_idx[j+1][1]
        return res