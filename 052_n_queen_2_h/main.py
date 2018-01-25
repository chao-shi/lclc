class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        # pass attack band because it is hard to do reversely, so storing as global var is bad
        def recur(row, down_attack, left_attack, right_attack):
            if row == n:
                self.res += 1
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
        
        self.res = 0
        board = [["."] * n for i in range(n)]
        recur(0, [False] * n, [False] * n, [False] * n)
        return self.res

# Very very careful: needs to use self.res.
# Code will break if replace with res
# then line 10 res += 1
# will intepret res as a different local variable
# Even if we try to print right the entry point of recur, res is undefined

# See more at 13.7 @
# https://www.protechtraining.com/content/python_fundamentals_tutorial-functional_programming