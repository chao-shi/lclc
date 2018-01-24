class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        cel = [set() for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    v = board[i][j]
                    celnum = (i/3) * 3 + j/3
                    row[i].add(int(v))
                    col[j].add(int(v))
                    cel[celnum].add(int(v))

        def searchNext():
            mini, minj, mincands, finished = -1, -1, None, True

            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        finished = False
                        celnum = (i/3) * 3 + j/3
                        cands = [c for c in range(1, 10) if c not in row[i] and c not in col[j] and c not in cel[celnum]]
                        if mincands == None or len(cands) < len(mincands):
                            mini, minj, mincands = i, j, cands
                            
            return mini, minj, mincands, finished
        
        def recur():
            i, j, cands, finished = searchNext()
            celnum = (i/3) * 3 + j/3

            if finished:
                return True
            for cand in cands:
                board[i][j] = str(cand)
                row[i].add(cand)
                col[j].add(cand)
                cel[celnum].add(cand)
                if recur():
                    return True
                board[i][j] = '.'
                row[i].remove(cand)
                col[j].remove(cand)
                cel[celnum].remove(cand)
            return False
        
        recur()