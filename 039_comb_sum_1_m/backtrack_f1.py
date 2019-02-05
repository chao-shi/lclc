class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates, reverse=True)
        hm = {}
        def recur(i, remain):
            if (i, remain) in hm:
                return hm[(i, remain)]
            elif remain == 0:
                return [[]]
            elif remain < 0 or i >= len(candidates):
                return []
            else:
                res = []
                res.extend([candidates[i]] + combo  for combo in recur(i, remain - candidates[i]))
                res.extend(recur(i + 1, remain))
                hm[(i, remain)] = res
                return res
        return recur(0, target)            
            