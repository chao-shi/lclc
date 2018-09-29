class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Keep (s, t) of current 1 seg and last one
        max_win = 0
        last_s, last_t = None, None
        cur_s, cur_t = None, None
        for i, num in enumerate(nums):
            if num == 1:
                if cur_s == None:
                    cur_s = i
                cur_t = i + 1
                # flip 0 before 1 seg
                max_win = max(max_win, cur_t - cur_s + (1 if cur_s > 0 else 0))
                
                # flip 0 in between
                if last_t != None and last_t + 1 == cur_s:
                    max_win = max(max_win, cur_t - last_s)
            else:
                if cur_s != None:
                    # flip 0 after 1 seg
                    max_win = max(max_win, cur_t - cur_s + 1)
                last_s, last_t = cur_s, cur_t
                cur_s, cur_t = None, None
                max_win = max(max_win, 1)
        return max_win
                
# Don't forget case 23
# Works for stream