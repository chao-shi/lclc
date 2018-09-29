class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mt = {}
        def recur(i, j):
            if i == j :
                return 0
            elif i + 1 == j:
                return nums[i]
            elif (i, j) in mt:
                return mt[(i, j)]
            else:
                val = max(nums[i] - recur(i+1, j), nums[j-1] - recur(i, j-1))
                mt[(i, j)] = val
                return val
        
        # corner case [] handled by line 9
        return recur(0, len(nums)) >= 0
        