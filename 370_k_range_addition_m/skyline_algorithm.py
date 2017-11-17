# 242 ms
class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        deltas = {}
        for update in updates:
            deltas[update[0]] = deltas.get(update[0], 0) + update[2]
            deltas[update[1] + 1] = deltas.get(update[1] + 1, 0) - update[2]
        
        res = [0] * length
        accu = 0
        for i in range(length):
            accu += deltas.get(i, 0)
            res[i] = accu
        return res

# Brute force o(K*N)

# Wrong Thought 1:
# If N >> K, then O(K*N) is constant, so no need to optimize
# Wrong in this specific case. Linear factor still matters here. 
# It makes difference in terms of how many reads of N size array

# Our algorithm O(K + N)

# Thought 2:
# No need to sort the critical points here