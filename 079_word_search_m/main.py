class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False

        m, n = len(board), len(board[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()

        def recur(i, j, k):
            if k == len(word):
                return True
            elif not 0 <= i < m or not 0 <= j < n or (i, j) in visited:
                return False
            elif board[i][j] != word[k]:
                return False
            else:
                visited.add((i, j))
                for v in dirs:
                    if recur(i + v[0], j + v[1], k + 1):
                        return True
                visited.remove((i, j))
                return False
        
        for i in range(m):
            for j in range(n):
                if recur(i, j, 0):
                    return True
        return False