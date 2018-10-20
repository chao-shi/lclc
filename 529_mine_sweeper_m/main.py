class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        m, n = len(board), len(board[0])
        vectors = ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))

        def inside(x, y):
            return 0 <= x < m and 0 <= y < n 
        
        def count_mine_adj(x, y):
            cnt = 0
            for v in vectors:
                xx, yy = x + v[0], y + v[1]
                if inside(xx, yy) and board[xx][yy] == 'M':
                    cnt += 1
            return cnt
        
        def reveal_avoid_mine(x, y):
            if not inside(x, y):
                pass
            elif board[x][y] == 'E':
                # not revealed empty
                cnt = count_mine_adj(x, y)
                if cnt > 0:
                    board[x][y] = str(cnt)
                else:
                    board[x][y] = 'B'
                    for v in vectors:
                        reveal_avoid_mine(x + v[0], y + v[1])
        
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            reveal_avoid_mine(x, y)
            
        return board
            
        
# reveal_avoid_mine does not reveal mine. Reveal mine is done out side recursion