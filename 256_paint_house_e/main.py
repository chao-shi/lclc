class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        cost_vector = [0] * 3
        for k in range(len(costs)):
            cost_vector = [costs[k][i] + min(cost_vector[j] for j in range(3) if i != j) for i in range(3)]
        return min(cost_vector)