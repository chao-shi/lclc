class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        last_row = [0] * n
        
        for i in range(m):
            cur_row = board[i][:]
            for j in range(n):
                cnt = sum(last_row[j + delta] for delta in range(-1, 2) if 0 <= j + delta < n)
                cnt += sum(cur_row[j + delta] for delta in range(-1, 2) if 0 <= j + delta < n)
                if i + 1 < m:
                    cnt += sum(board[i+1][j + delta] for delta in range(-1, 2) if 0 <= j + delta < n)
                cnt -= board[i][j]
                if (board[i][j] == 1 and (cnt < 2 or cnt > 3)) or (board[i][j] == 0 and cnt == 3):
                    board[i][j] = 1 - board[i][j]

            last_row = cur_row
            
# No good in place solution, all the answers in the forum are using some magic number to represent two information
# in each cell slot