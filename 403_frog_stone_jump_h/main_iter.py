class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        hm = {}
        dest = stones[-1]
        for s in stones:
            hm[s] = set()
        hm[0].add(0)

        for i, s in enumerate(stones):
            # Aggregate the next_step together. Where I missed in the beginning BF DFS
            next_steps = set([d + last_step for d in [-1, 0, 1] for last_step in hm[s] if d + last_step > 0])
            for next_step in next_steps:
                next_stone = next_step + s
                if next_stone in hm:
                    hm[next_stone].add(next_step)
        
        return len(hm[dest]) > 0