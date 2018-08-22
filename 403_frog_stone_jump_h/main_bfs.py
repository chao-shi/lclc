class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        dest = stones[-1]
        stones = set(stones)
        options = collections.deque()
        options.append((0, 0))
        
        # Add visited for BFS
        visited = set([(0, 0)])

        while options:
            op = options.popleft()
            if op[1] == dest:
                return True

            for d in [-1, 0, 1]:
                next_step = op[0] + d
                next_p = op[1] + next_step
                if next_step > 0 and next_p in stones and (next_step, next_p) not in visited:
                    options.append((next_step, next_p))
                    visited.add((next_step, next_p))
        return False