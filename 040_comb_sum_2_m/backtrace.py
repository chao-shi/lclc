class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        counter = collections.Counter(candidates)
        candidates = sorted(set(candidates), reverse=True)
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
                used = 0
                while used * candidates[i] <= remain and used <= counter[candidates[i]]:
                    res.extend([candidates[i]] * used + combo  for combo in recur(i + 1, remain - used * candidates[i]))
                    used += 1
                hm[(i, remain)] = res
                return res
        return recur(0, target)      
            