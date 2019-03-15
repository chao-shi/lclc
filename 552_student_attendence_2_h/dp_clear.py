class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        # "", ["L", "P"], ...
        no_a = [1, 2, 4]
        for i in range(3, n+1):
            # P
            cnt = no_a[-1]
            # PL
            cnt += no_a[-2]
            # PLL
            cnt += no_a[-3]
            no_a.append(cnt%(10**9 + 7))
             
        a = [1, 3, 8]
        for i in range(3, n+1):
            # A
            cnt = no_a[i-1] #LLA, LPA, PLA, PPA 4
            # P
            cnt += a[-1] #8
            # PL and AL
            cnt += a[-2] + no_a[i-2] #2
            # PLL and ALL
            cnt += a[-3] + no_a[i-3]
            a.append(cnt%(10**9 + 7))
        return a[n]

# Second time implementing, expend a and no_a