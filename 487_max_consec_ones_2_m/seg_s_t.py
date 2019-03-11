class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        anchor = -1
        maxv = 0
        last_win = None
        for i in range(len(nums) + 1):

            if i == len(nums) or nums[i] == 0:
                seg_len = i - anchor - 1
                
                maxv = max(maxv, seg_len)
                if anchor >= 0 or i < len(nums):
                    maxv = max(maxv, seg_len + 1)    
                
                if last_win != None:
                    s, t = last_win
                    if t == anchor:
                        maxv = max(maxv, seg_len + 1 + t - s)

                last_win = (anchor + 1, i)
                anchor = i
        return maxv