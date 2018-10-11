class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        accu_sum = 0
        self.rects = rects
        self.accu_map = [0]
        for r in rects:
            accu_sum += (r[2] - r[0] + 1) * (r[3] - r[1] + 1)
            self.accu_map.append(accu_sum)

    def pick(self):
        """
        :rtype: List[int]
        """
        ra = random.randint(0, self.accu_map[-1] - 1)
        idx = bisect.bisect_right(self.accu_map, ra) - 1
        x1, y1 = self.rects[idx][0], self.rects[idx][1]
        x2, y2 = self.rects[idx][2], self.rects[idx][3]
        return [random.randint(x1, x2), random.randint(y1, y2)]



# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
# 
# Simple for non-overlapping
# Pick a rect and pick a point inside.
# 
# Follow up: Overlapping, 
# For each x, a subproblem of merge intervals