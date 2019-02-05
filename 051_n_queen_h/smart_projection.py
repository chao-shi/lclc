class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # pass attack band because it is hard to do reversely, so storing as global var is bad
        # This is smart approach, we store the left/right projection on the first row of each placed queue
        # For example, queue on row 2 col 3 plays as if it is left attacking from row 1 col 2
        def recur(row, down_project, left_project, right_project):
            if row == n:
                res.append(["".join(row) for row in board])
                return

            for i in range(n):
                if i not in down_project and i - row not in left_project and i + row not in right_project:
                    board[row][i] = 'Q'
                    down_project.add(i)
                    left_project.add(i - row)
                    right_project.add(i + row)
                    recur(row + 1, down_project, left_project, right_project)
                    board[row][i] = '.'
                    down_project.remove(i)
                    left_project.remove(i - row)
                    right_project.remove(i + row)
        
        res = []
        board = [["."] * n for i in range(n)]
        recur(0, set(), set(), set())
        return res
# Careful Careful, don't early return on line 24. No need to return True/False.
# Return True/False if the question is asking to find one solution

# Smart projection, very good solution by me. Beats 96%