class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board:
            return 0
        
        def upper_empty(i, j):
            return i == 0 or board[i-1][j] == '.'
        
        def left_empty(i, j):
            return j == 0 or board[i][j-1] == '.'

        m, n = len(board), len(board[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and upper_empty(i, j) and left_empty(i, j):
                    cnt += 1
        return cnt
                