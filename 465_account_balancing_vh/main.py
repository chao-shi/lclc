class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        def remove_one_zero_clique(non_zero):
            n = len(non_zero)
            q = collections.deque()            
            # q store ([index set], sum of set)
            q.append(([0], non_zero[0]))
            min_zero_set = None

            while q:
                cur_set, cur_sum = q.popleft()
                if cur_sum == 0:
                    min_zero_set = cur_set
                    break
                for j in range(cur_set[-1] + 1, n):
                    q.append((cur_set + [j], cur_sum + non_zero[j]))
            
            min_zero_set = set(min_zero_set)
            return [non_zero[i] for i in range(n) if i not in min_zero_set]
        
        
        bal = collections.defaultdict(int)
        for t in transactions:
            bal[t[0]] -= t[2]
            bal[t[1]] += t[2]
        non_zero = [bal[k] for k in bal if bal[k] != 0]
        
        bal_cnt = len(non_zero)
        while len(non_zero) > 0:
            non_zero = remove_one_zero_clique(non_zero)
            bal_cnt -= 1
        return bal_cnt

# Figure out by myself, beats 100% !! 
# Better and easier than DFS provided online.
# 
# https://leetcode.com/problems/optimal-account-balancing/discuss/95355/11-liner-9ms-DFS-solution-(detailed-explanation)
# Greedy DFS
# start with i, as recur, try to find the first opposite sign number to cancel out nums[i]