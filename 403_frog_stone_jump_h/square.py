class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        dest = stones[-1]
        cands = set([(0, 0)])

        for i, s in enumerate(stones):
            for j in range(i):
                step = s - stones[j]
                for d in [-1, 0, 1]:
                    last_step = step + d
                    if (stones[j], last_step) in cands:
                        cands.add((s, step))
                        if s == dest:
                            return True
        return False

# A not so good solution but guaranteed N^2 bounded.
# Does not find quick solutions like DFS.