class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rows = [[] for i in range(numRows)]
        cur_row = 0
        dir_down = True
        for i, ch in enumerate(s):
            rows[cur_row].append(ch)
            if numRows == 1:
                pass
            elif cur_row == numRows - 1:
                cur_row -= 1
                dir_down = False
            elif cur_row == 0 and not dir_down:
                cur_row += 1
                dir_down = True
            elif dir_down:
                cur_row += 1
            else:
                cur_row -= 1
        return "".join(["".join(row) for row in rows])

# y index does not matter here, just need to update cur_row accordingly
# careful line 13 and line 18 check dir_down