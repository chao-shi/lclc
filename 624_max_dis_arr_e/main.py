class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        arr_max = map(lambda x:x[-1], arrays)
        max2 = sorted(arr_max, reverse=True)[:2]
        res = 0
        for i in range(len(arrays)):
            max_dis = abs(arrays[i][0] - (max2[1] if arrays[i][-1] == max2[0] else max2[0]))
            res = max(res, max_dis)
        return res
    
# The answer has to one first element and one last element
# For each first element, check maximum last element except in the same array