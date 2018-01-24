class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        counter = collections.Counter(candidates)
        candidates = [(key, counter.get(key)) for key in counter]

        m = [[[] for j in range(len(candidates) + 1)] for i in range(1+target)]
        for i in range(len(candidates) + 1):
            m[0][i].append([])
        
        for i in range(1, target + 1):
            for j in range(1, len(candidates) + 1):
                for ii in range(candidates[j-1][1] + 1):
                    remain = i - ii * candidates[j-1][0]
                    if remain >= 0:
                        m[i][j].extend([comb + [candidates[j-1][0]] * ii for comb in m[remain][j-1]])
                    else:
                        break
        return m[target][len(candidates)]

# Careful: Line 20 needs expansion

# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
# A solution set is: 
#
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]

# If treat every element differently, we might count [1,7] more than once. Careful

# backtrace should also work. Omitting here.