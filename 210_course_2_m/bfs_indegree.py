class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        preq_cnt = {}
        precede_map = {}
        for a, b in prerequisites:
            preq_cnt[a] = preq_cnt.get(a, 0) + 1
            precede_map.setdefault(b, []).append(a)

        # no need for set, finer controller for insertion
        no_deps = [i for i in range(numCourses) if preq_cnt.get(i, 0) == 0]
        seq = []
        
        while no_deps:
            top = no_deps.pop()
            seq.append(top)
            for after in precede_map.get(top, []):
                preq_cnt[after] -= 1
                if preq_cnt[after] == 0:
                    no_deps.append(after)
        
        if len(seq) != numCourses:
            return []
        return seq