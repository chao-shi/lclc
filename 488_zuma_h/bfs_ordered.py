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


        def get_next_hands(hand):
            res = set()
            for i in range(len(hand)):
                res.add((hand[i], hand[:i] + hand[i+1:]))
            return res

        hand = str(sorted(hand))
        q = collections.deque()
        q.append((board, hand))
        visited = set((board, hand))

        level = 0
        while q:
            for i in range(len(q)):
                cur_board, cur_hand = q.popleft()

                if cur_board == "":
                    return level

                for ball, next_hand in get_next_hands(cur_hand):
                    for next_board in map(merge, insert(cur_board, ball)):
                        if (next_board, next_hand) not in visited:
                            visited.add((next_board, next_hand))
                            q.append((next_board, next_hand))
            level += 1
        return -1