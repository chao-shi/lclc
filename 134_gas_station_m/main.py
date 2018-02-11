class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        i, j = 0, 0
        n = len(gas)
        tank = 0
        for k in range(n):
            if tank + gas[j] - cost[j] >= 0:
                tank += gas[j] - cost[j]
                j = (j + 1) % n
            else:
                i = (i - 1) % n
                tank += gas[i] - cost[i]
        return -1 if tank < 0 else i
        