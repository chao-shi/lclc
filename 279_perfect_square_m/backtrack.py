class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.min_cnt = n

        def recur(remain, used):
            if remain == 0:
                self.min_cnt = min(self.min_cnt, len(used))
                return

            i = used[-1] if used else 1
            while i * i <= remain:
                used.append(i)
                recur(remain - i * i, used)
                used.pop()
                i += 1
            
        recur(n, [])
        return self.min_cnt

# Too slow for OJ
# A lot of recompute, in case of 12 = 4 + 4 + 4