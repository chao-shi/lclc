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
                if not down_attack[i] and not left_attack[i] and not right_attack[i]:
                    board[row][i] = 'Q'
                    new_down_attack = down_attack[:i] + [True] + down_attack[i+1:] 
                    new_left_attack = [False] + left_attack[:n-1]
                    if i < n - 1:
                        new_left_attack[i+1] = True
                    new_right_attack = right_attack[1:] + [False]
                    if i > 0:
                        new_right_attack[i-1] = True
                    
                    recur(row + 1, new_down_attack, new_left_attack, new_right_attack)
                    
                    board[row][i] = '.'
        
        res = []
        board = [["."] * n for i in range(n)]
        recur(0, [False] * n, [False] * n, [False] * n)
        return res

# Careful Careful, don't early return on line 24. No need to return True/False.
# Return True/False if the question is asking to find one solution