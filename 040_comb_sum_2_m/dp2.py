class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates, reverse=True)
        # Meaning of m1 changed here, the combo the list of m[i][j] must end with candidates[j-1]
        m1 = [[[] for j in range(len(candidates) + 1)] for i in range(target+1)]
        # m2 is all, regardless of ending with j-1
        m2 = [[[] for j in range(len(candidates) + 1)] for i in range(target+1)]
        
        for i in range(len(candidates) + 1):
            m2[0][i].append([])
        # Correct init
        m1[0][0].append([])

        for i in range(1, target+1):
            for j in range(1, len(candidates) + 1):

                # Take j - 1, but you have two options based on if j - 1 is the first appearance for repeated numbers
                if i - candidates[j - 1] >= 0:
                    if j and candidates[j-1] == candidates[j-2]:
                        # If you take j-1, j-2 must be taken as well
                        m1[i][j].extend(combo + [candidates[j-1]] for combo in m1[i - candidates[j-1]][j-1])
                    else:
                        m1[i][j].extend(combo + [candidates[j-1]] for combo in m2[i - candidates[j-1]][j-1])
                
                m2[i][j].extend(m1[i][j])
                m2[i][j].extend(m2[i][j-1])
                            
        return m2[target][len(candidates)]
    
# Careful initialization on line 8