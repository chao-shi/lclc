import math
class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        m = {}
        for i in range(1, n+1):
            if n % i != 0:
                continue
            res_i = []
            for first_factor in range(2, int(math.sqrt(i)) + 1):
                if i % first_factor != 0:
                    continue
                res_i.extend([first_factor] + combo for combo in m[i / first_factor] if first_factor <= combo[0])
                res_i.append([first_factor, i / first_factor])
            m[i] = res_i
        return m[n]

# Does not pass Memory limit for line 8
# Does not pass Time because dp is bad for the following case

# print Solution().getFactors(23848713)
# with factors 
# 1
# 3
# 7
# 9
# 21
# 63
# 378551
# 1135653
# 2649857
# 3406959
# 7949571

# Line 9 is too slow.