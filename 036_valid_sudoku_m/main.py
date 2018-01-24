class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        cel = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    v = board[i][j]
                    celnum = (i/3) * 3 + j/3
                    if v in row[i] or v in col[j] or v in cel[celnum]:
                        return False
                    row[i].add(v)
                    col[j].add(v)
                    cel[celnum].add(v)
        return True
                        
        