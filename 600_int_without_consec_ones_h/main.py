class Solution(object):
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        b = bin(num)[2:]
        n = len(b)
        
        # Number of possible numbers without continous 1 with length L
        cnt_by_len = [1] * (n + 1)
        cnt_by_len[1] = 2
        
        for i in range(1, n + 1):
            cnt_by_len[i] = cnt_by_len[i-1] + cnt_by_len[i-2]
        
        # For each 1 bit, we have the choice of make it 0 and make the rest n - i - 1 bits 
        # satisfying non-continous limitation
        # Each round the prefix is different, so no overlapping
        res = 0
        for i in range(n):
            if b[i] == "1" and "11" not in b[:i]:
                res += cnt_by_len[n-1-i]
                
        # Don't forget corner case check number itself
        if "11" not in b:
            res += 1
        return res