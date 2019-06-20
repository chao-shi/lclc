class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        prob_map = {0: 1}
        for i in range(K):
            new_prob_map = collections.defaultdict(int)
            for ptr in prob_map:
                if ptr >= K:
                    new_prob_map[ptr] += prob_map[ptr]
                else:
                    for j in range(1, W + 1):
                        new_prob_map[ptr + j] += float(prob_map[ptr]) / float(W)
            prob_map = new_prob_map
        
        dist = [prob_map[ptr] for ptr in prob_map if ptr <= N]
        if dist:
            return sum(dist)
        else:
            return 0