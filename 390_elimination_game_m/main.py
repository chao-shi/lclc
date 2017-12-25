# Keep state of start, end, diff

class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end, diff = 1, n , 1
        while start < end:
            # forward
            if (end - start) % (2 * diff) == 0:
                # last eliminated
                end -= diff
            start += diff
            diff *= 2
            
            if start == end:
                return start
            
            # backward
            if (end - start) % (2 * diff) == 0:
                start += diff
            end -= diff
            diff *= 2
        
        return start