class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        if any(ch not in " OX" for ch in "".join(board)):
            return False
        cntX = sum(map(lambda x:x.count("X"), board))
        cntO = sum(map(lambda x:x.count("O"), board))
        if cntX - cntO > 1 or cntX - cntO < 0:
            return False

        consec3 = board + ["".join([board[i][j] for i in range(3)]) for j in range(3)] \
            + ["".join([board[i][i] for i in range(3)]), "".join([board[i][2-i] for i in range(3)])]

        winX = consec3.count("XXX")
        winO = consec3.count("OOO")
        
        # Don't check the sum, the winX can be bigger than 1
        if winX > 0 and winO > 0:
            return False
        elif winX > 0:
            return cntX - cntO == 1
        elif winO > 0:
            return cntO - cntX == 0
        else:
            return True

# REVISIT, TOO MANY CORNER CASES