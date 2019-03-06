class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        elements = set()
        ratio_map = collections.defaultdict(dict)
        for i, e in enumerate(equations):
            elements.add(e[0])
            elements.add(e[1])
            ratio_map[e[0]][e[1]] = values[i]
            ratio_map[e[1]][e[0]] = 1.0 / values[i]
        
        
        def recur(cur, divisor, visited):
            if cur == divisor:
                return 1.0
            elif cur in visited:
                return -1.0

            visited.add(cur)
            for n in ratio_map[cur]:
                ret = recur(n, divisor, visited)
                if ret != -1.0:
                    return ret * ratio_map[cur][n]
            visited.remove(cur)
            return -1.0

        
        res = []
        for q in queries:
            if q[0] not in elements or q[1] not in elements:
                res.append(-1.0)
            else:
                res.append(recur(q[0], q[1], set()))
        return res

# Follow up, what if there are zeros. Then keep those zero elements as separate. If divident is zero, return zero, if
# divisor is zero, return invalid