class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # pass attack band because it is hard to do reversely, so storing as global var is bad
        def recur(row, down_attack, left_attack, right_attack):
            if row == n:
                res.append(["".join(row) for row in board])
                return

            for i in range(n):
                if i not in down_attack and i not in left_attack and i not in right_attack:
                    board[row][i] = 'Q'
                    new_down = set(down_attack)
                    new_down.add(i)
                    new_left = set(ii + 1 for ii in left_attack if ii + 1 < n)
                    if i + 1 < n:
                        new_left.add(i + 1)
                    new_right = set(ii - 1 for ii in right_attack if ii - 1 >= 0)
                    if i - 1 >= 0:
                        new_right.add(i - 1)
                    recur(row + 1, new_down, new_left, new_right)
                    
                    board[row][i] = '.'
        
        res = []
        board = [["."] * n for i in range(n)]
        recur(0, set(), set(), set())
        return res
# Careful Careful, don't early return on line 24. No need to return True/False.
# Return True/False if the question is asking to find one solution