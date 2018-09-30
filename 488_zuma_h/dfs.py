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
        
        def recur(board, unused):
            if board == "":
                self.ans = min(self.ans, len(hand) - len(unused))
                return 

            for i in range(len(unused)):
                next_boards = map(merge, insert(board, unused[i]))
                for nb in next_boards:
                    recur(nb, unused[:i] + unused[i+1:])
        
        self.ans = len(hand) + 1
        recur(board, hand)
        return self.ans if self.ans <= len(hand) else -1