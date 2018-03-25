class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        preq_map = {}
        for a, b in prerequisites:
            preq_map.setdefault(a, []).append(b)
        visited = {}
        seq = []

        def recur(root):
            if visited.get(root, None) == 0:
                return False
            elif visited.get(root, None) == 1:
                return True
            
            visited[root] = 0
            for preq in preq_map.get(root, []):
                if not recur(preq):
                    return False
            visited[root] = 1
            seq.append(root)
            return True
                
        for i in range(numCourses):
            if not recur(i):
                return []
        return seq