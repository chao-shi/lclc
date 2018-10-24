class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        gap_cnt = collections.defaultdict(int)
        for row in wall:
            x = 0
            for i in range(len(row) - 1):
                brick = row[i]
                x += brick
                gap_cnt[x] += 1
                
        if len(gap_cnt) == 0:
            return len(wall)
        else:
            return len(wall) - max(gap_cnt.values())