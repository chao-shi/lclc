class Excel(object):

    def __init__(self, H, W):
        """
        :type H: int
        :type W: str
        """
        self.h, self.w = H, ord(W) - ord('A') + 1
        self.cells = [[0] * self.w for _ in range(H)]
        # sum_map is like sum contribution map
        # If B2 = A1 + A2, then A1 and A2 will be key in sum_map
        # value will be {B2: 1}
        self.sum_map = collections.defaultdict(lambda : collections.defaultdict(int))

        
    # Complexity O(RC)
    def set(self, r, c, v):
        """
        :type r: int
        :type c: str
        :type v: int
        :rtype: void
        """
        i, j = rc_to_idx(r, c)
        delta = v - self.cells[i][j]
        # self.cells[i][j] = v
        
        # Corner case forgot, disconnect
        for rr, cc in self.sum_map:
            if (r, c) in self.sum_map[(rr, cc)]:
                self.sum_map[(rr, cc)].pop((r, c))
        
        seq = self.topo_sort(r, c)
        update_map = collections.defaultdict(int)
        update_map[(r, c)] = 1
        for rr, cc in seq:
            mul = update_map[(rr, cc)]
            for rn, cn in self.sum_map[(rr, cc)]:
                update_map[(rn, cn)] += mul * self.sum_map[(rr, cc)][(rn, cn)] 
        
        for rr, cc in update_map:
            i, j = rc_to_idx(rr, cc)
            self.cells[i][j] += update_map[(rr, cc)] * delta
        

    # Sort all cells which are impacted by change of r, c
    def topo_sort(self, r, c):
        res = []
        self.topo_sort_helper(r, c, res, set())
        return res[::-1]
        
        
    def topo_sort_helper(self, r, c, res, visited):
        if (r, c) in visited:
            return
        visited.add((r, c))
        for rr, cc in self.sum_map[(r, c)]:
            self.topo_sort_helper(rr, cc, res, visited)
        res.append((r, c))
        

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
                self.sum_map[(rr, cc)][(r, c)] += 1
        
        i, j = rc_to_idx(r, c)
        self.cells[i][j] = sumv
        return sumv
            
        
def rc_to_idx(r, c):
    return r - 1, ord(c) - ord('A')


def rect_cells(r1, c1, r2, c2):
    res = []
    for r in range(r1, r2 + 1):
        for c in range(ord(c1), ord(c2) + 1):
            res.append((r, chr(c)))
    return res

def split_cell(cell):
    return int(cell[1:]), cell[0]

# Your Excel object will be instantiated and called as such:
# obj = Excel(H, W)
# obj.set(r,c,v)
# param_2 = obj.get(r,c)
# param_3 = obj.sum(r,c,strs)

# Topology sorting + value update map
# Example case: B = A, C = 2* A, D = 2 * B + 2 * A + C
# Store the above structure in sum_map
# sum_map = {A: {B: 1, C:2, D:2}, B:{D: 2}, C:{D: 1}}
# First topology sort [A, B, C, D]
# update_map = {A: 1}

# Process A, A is depended on by B, C, D, 
# update_map = {A: 1, B: 1, C: 2, D:2}

# Process B, B is depended by D with multiplier of 2, 
# B is 1 multiple of A delta, then D is 2 of A delta
# update_map = {A: 1, B: 1, C: 2, D:2 + 2}

# Process C, 
# update_map = {A: 1, B: 1, C: 2, D: 2+ 2+ 2}

# Done with process