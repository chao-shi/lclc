class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        m = [[[] for j in range(len(candidates) + 1)] for i in range(target+1)]
        for i in range(len(candidates) + 1):
            m[0][i].append([])
        
        for i in range(1, target+1):
            for j in range(1, len(candidates) + 1):
                m[i][j].extend(m[i][j-1])
                if i >= candidates[j-1]:
                    m[i][j].extend([comb + [candidates[j-1]] for comb in m[i-candidates[j-1]][j]])
                    
        return m[target][len(candidates)]
    
# Careful initialization on line 8