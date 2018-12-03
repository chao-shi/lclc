class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        lb, hb = 1, m * n 
        
        while lb <= hb:
            mid = (lb + hb) / 2
            j1, j2 = n, n
            cnt_l, cnt_le = 0, 0
            for i in range(1, m + 1):
                while j2 > 0 and i * j2 > mid:
                    j2 -= 1
                while j1 > 0 and i * j1 >= mid:
                    j1 -= 1
                cnt_l += j1
                cnt_le += j2

            if cnt_l < k <= cnt_le:
                return mid
            elif k <= cnt_l:
                hb = mid - 1
            else:
                lb = mid + 1
                
# Finding j1, j2 can be optmized using math.
# See solution