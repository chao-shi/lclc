class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        def out_of_range(x, y):
            return x < 0 or x >= R or y < 0 or y >= C

        vs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        d = 0
        cur = [r0, c0]
        step = 1
        res = []
        while len(res) < R * C:
            next_cur_x = cur[0] + vs[d][0] * step
            next_cur_y = cur[1] + vs[d][1] * step
            
            for k in range(step):
                x, y = cur[0] + vs[d][0] * k, cur[1] + vs[d][1] * k
                if not out_of_range(x, y):
                    res.append([x, y])
            
            cur = [next_cur_x, next_cur_y]
            
            if d % 2 == 1:
                step += 1
            d  = (d + 1) % 4
        return res
    
# Complexity is max(R, C) ** 2 (Cannot go beyond border too much)