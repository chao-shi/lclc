class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def distance(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        
        cnt = 0
        for i, p_i in enumerate(points):
            dis_map = {}
            for j, p_j in enumerate(points):
                if j != i:
                    dis = distance(p_i, p_j)
                    cnt += dis_map.get(dis, 0) * 2
                    dis_map[dis] = dis_map.get(dis, 0) + 1
        return cnt