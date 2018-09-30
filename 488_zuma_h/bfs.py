class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        # Case of BBAABB with BA in hands, needs to give up B
        # Two options, insert next to same color
        # Or don't insert
        def insert(board, new_ball):
            res = []
            for i, ball in enumerate(board):
                if ball == new_ball and (i == 0 or board[i-1] != ball):
                    res.append(board[:i] + new_ball + board[i:])
                    
            return res
        
        def merge(board):
            while True:
                new_board = None
                for i in range(len(board)):
                    j = i + 1
                    while j < len(board) and board[j] == board[i]:
                        j += 1
                    if j - i >= 3:
                        new_board = board[:i] + board[j:]
                        break
                if new_board == None:
                    return board
                else:
                    board = new_board
                    
        q = []
        q.append((board, 0))
        visited = set([board])
        
        for i in range(len(hand)):
            q_len = len(q)
            for j in range(len(q)):
                # boards are all outcomes using up to hand[:i]
                boards, cnt = q[j]
                next_boards = map(merge, insert(boards, hand[i]))
                for nb in next_boards:
                    if nb not in visited:
                        # no need to insert if seen before, cnt + 1 must be bigger than previous seen
                        # which is less optimal solution.
                        visited.add(nb)
                        q.append((nb, cnt + 1))
            
            valid_cnts = [q[ii][1] for ii in range(q_len, len(q)) if q[ii][0] == ""]
            if valid_cnts:
                return min(valid_cnts)

        return -1

# BFS 
# Failed test case
# "WRYYRWWRRWW", "WYBR"
# I though you must use the hand in order.

                