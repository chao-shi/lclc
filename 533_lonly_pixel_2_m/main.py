class Solution(object):
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        value_map = {}
        row_encoded = []
        for row in picture:
            row_str = "".join(row)
            if row_str not in value_map:
                value_map[row_str] = len(value_map) + 1
            row_encoded.append(value_map[row_str])

        m, n = len(picture), len(picture[0])
        # Don't write [set()] * n
        row, col = [0] * m, [set() for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    row[i] += 1
                    col[j].add(i)
        

        # We can precompute the validatation on vertical index
        # col[j] store the list of rows ii such that picture[ii][j] is black,
        # We precheck if all those rows are same
        col_valid = [False] * n
        for j in range(n):
            if len(col[j]) == N:
                if len(set([row_encoded[ii] for ii in col[j]])) == 1:
                    col_valid[j] = True


        ans = 0
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B' and row[i] == N and col_valid[j]:
                    ans += 1
        return ans

        