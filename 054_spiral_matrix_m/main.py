class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])
        x, y = 0, 0
        h_step, v_step = n, m - 1
        res = []
        v = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        while len(res) < m * n:
            for dir in range(4):
                step = h_step if dir % 2 == 0 else v_step

                if step == 0:
                    return res

                for i in range(step):
                    res.append(matrix[x][y])
                    x, y = x + v[dir][0], y + v[dir][1]

                next_dir = (dir + 1) % 4
                # step back one and step forward one
                x, y = x + -v[dir][0] + v[next_dir][0], y -v[dir][1] + v[next_dir][1]
                
                if dir % 2 == 0:
                    h_step -= 1
                else:
                    v_step -= 1
        return res

# Explained for example
# 1, 2,  3,  4
# 5, 6,  7,  8
# 9, 10, 11, 12

# How to batch it 
# Row: 1, 2, 3, 4
# Col: 8, 12
# Row: 11, 10, 9
# Col: 5
# Row: 6, 7
# Col: Exit here, since the length is zero 
# h_step and v_step reduce by 1 each round.