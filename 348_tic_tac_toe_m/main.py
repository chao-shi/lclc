class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.h = [[0, 0] for _ in range(n)]
        self.v = [[0, 0] for _ in range(n)]
        self.d = [[0, 0], [0, 0]]

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.h[row][player-1] += 1
        self.v[col][player-1] += 1
        if row == col:
            self.d[0][player-1] += 1
        if row + col == self.n - 1:
            self.d[1][player-1] += 1
        
        for arr in [self.h[row], self.v[col], self.d[0], self.d[1]]:
            if arr[player-1] == self.n:
                return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)