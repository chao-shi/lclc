from collections import deque
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        mulmap = {}
        eles = set()
        for i in range(len(equations)):
            eq = equations[i]
            eles.add(eq[0])
            eles.add(eq[1])
            if eq[1] not in mulmap:
                mulmap[eq[1]] = {}
            if eq[0] not in mulmap:
                mulmap[eq[0]] = {}
            mulmap[eq[1]][eq[0]] = values[i]
            mulmap[eq[0]][eq[1]] = 1.0/values[i]


        def process(dividend, divisor):
            if dividend not in eles or divisor not in eles:
                return -1.0

            queue = deque([(divisor, 1)])
            visited = set([divisor])
            while queue:
                tp = queue.popleft()
                if tp[0] == dividend:
                    return tp[1]
                nextmap = mulmap.get(tp[0], {})
                for n in nextmap:
                    if n not in visited:
                        visited.add(n)
                        multiplier = tp[1] * nextmap[n]
                        queue.append((n, multiplier))
                        
            return -1.0

        return [process(q[0], q[1]) for q in queries]

# Notice

# Graph BFS

# Build bi-directional graph.

# Line 25 check if two elements are in valid. if query is ['x', 'x'] and 'x' is not valid, we should return -1

# Cannot move block 32 under block 36, ['a', 'a'] will fail

# The assumption is that there is no contradiction. How to check contradiction is a follow-up

# If pre-processing needed.
# 1. if number of queries more than O(N^2), we can preprocess all pairs.
# 2. if number of queries more than O(N), can we pick one root PER COMPONENT and keep the multiplier for each element. 
#    If two elements belong two components, they will have different root picked
# 3. if number of queries is small, process each query without global state
