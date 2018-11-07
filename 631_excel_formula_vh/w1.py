class Excel(object):

    def __init__(self, H, W):
        """
        :type H: int
        :type W: str
        """
        self.h, self.w = H, ord(W) - ord('A') + 1
        self.cells = [[0] * self.w for _ in range(H)]
        self.sum_map = {}

    def set(self, r, c, v):
        """
        :type r: int
        :type c: str
        :type v: int
        :rtype: void
        """
        i, j = rc_to_idx(r, c)
        delta = v - self.cells[i][j]
        self.cells[i][j] = v
        
        # Corner case forgot
        if (r, c) in self.sum_map:
            self.sum_map.pop((r, c))
        
        for rs, cs in self.sum_map:
            isum, jsum = rc_to_idx(rs, cs)
            for r1, c1, r2, c2 in self.sum_map[(rs, cs)]:
                if inside(r, c, r1, c1, r2, c2):
                    self.cells[isum][jsum] += delta


    def get(self, r, c):
        """
        :type r: int
        :type c: str
        :rtype: int
        """
        i, j = rc_to_idx(r, c)
        return self.cells[i][j]
        

    def sum(self, r, c, strs):
        """
        :type r: int
        :type c: str
        :type strs: List[str]
        :rtype: int
        """
        sumv = 0
        rects = []
        for s in strs:
            if ":" not in s:
                r1, c1= split_cell(s)
                r2, c2 = r1, c1
            else:
                r1, c1 = split_cell(s.split(":")[0])
                r2, c2 = split_cell(s.split(":")[1])
            
            for rr, cc in rect_cells(r1, c1, r2, c2):
                i, j = rc_to_idx(rr, cc)
                sumv += self.cells[i][j]
            rects.append((r1, c1, r2, c2))
        
        i, j = rc_to_idx(r, c)
        self.cells[i][j] = sumv
        self.sum_map[(r, c)] = rects
        return sumv
            
        
def rc_to_idx(r, c):
    return r - 1, ord(c) - ord('A')


def rect_cells(r1, c1, r2, c2):
    res = []
    for r in range(r1, r2 + 1):
        for c in range(ord(c1), ord(c2) + 1):
            res.append((r, chr(c)))
    return res

def inside(r, c, r1, c1, r2, c2):
    return r1 <= r <= r2 and c1 <= c <= c2

def split_cell(cell):
    return int(cell[1:]), cell[0]

# Your Excel object will be instantiated and called as such:
# obj = Excel(H, W)
# obj.set(r,c,v)
# param_2 = obj.get(r,c)
# param_3 = obj.sum(r,c,strs)
# 
# This flat approach is wrong, For example
# C5 = sum(A1:A5)
# A3 = sum(B1:B2)
# if B2 updates, C5 is not touched.