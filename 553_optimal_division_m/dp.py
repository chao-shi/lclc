class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        n = len(nums)
        mt_max = {}
        mt_min = {}
        for i in range(n):
            mt_max[(i, i+1)] = (float(nums[i]), str(nums[i]))
            mt_min[(i, i+1)] = (float(nums[i]), str(nums[i]))
        for l in range(2, n+1):
            for i in range(n-l+1):
                max_ans = (0, "")
                min_ans = (sys.maxint, "")
                j = i + l
                for k in range(i+1, j):
                    lv, le = mt_max[(i, k)]
                    rv, re = mt_min[(k, j)]
                    if lv / rv > max_ans[0]:
                        e = le + "/" + ("({})".format(re) if j - k > 1 else re)
                        max_ans = (lv / rv, e)
                        
                    lv, le = mt_min[(i, k)]
                    rv, re = mt_max[(k, j)]
                    if lv / rv < min_ans[0]:
                        e = le + "/" + ("({})".format(re) if j - k > 1 else re)
                        min_ans = (lv / rv, e)
                    
                mt_min[(i, j)] = min_ans
                mt_max[(i, j)] = max_ans
        return mt_max[(0, n)][1]