class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        x, y = 0, 0
        h_step, v_step = n, n - 1
        res = [[0] * n for i in range(n)]
        v = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        cur = 1

        while cur <= n * n:
            for dir in range(4):
                step = h_step if dir % 2 == 0 else v_step

                if step == 0:
                    return res

                for i in range(step):
                    res[x][y] = cur
                    x, y = x + v[dir][0], y + v[dir][1]
                    cur += 1

                next_dir = (dir + 1) % 4
                # step back one and step forward one
                x, y = x + -v[dir][0] + v[next_dir][0], y -v[dir][1] + v[next_dir][1]
                
                if dir % 2 == 0:
                    h_step -= 1
                else:
                    v_step -= 1
        return res