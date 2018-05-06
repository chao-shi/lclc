class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        def min2_index(l):
            min1, min2 = None, None
            for i, v in enumerate(l):
                if min1 == None or v < l[min1]:
                    min1, min2 = i, min1
                elif min2 == None or v < l[min2]:
                    min2 = i
            return [min1, min2]


        if not costs:
            return 0
        n, k = len(costs), len(costs[0])
        if k < 2 and n > 1:
            return False

        total_cost = [[0] * k for i in range(n)]
        min2col = [[0, 0] for i in range(n)]
        
        total_cost[0] = costs[0]
        min2col[0] = min2_index(costs[0]) 
        
        for i in range(1, n):
            for j in range(k):
                last_color = min2col[i-1][0] if min2col[i-1][0] != j else min2col[i-1][1]
                total_cost[i][j] = total_cost[i-1][last_color] + costs[i][j]
            min2col[i] = min2_index(total_cost[i])

        return total_cost[n-1][min2col[n-1][0]]
            
