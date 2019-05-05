class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        counter = collections.Counter(candidates)
        uniq_candidates = sorted(counter.keys(), reverse=True)
        print uniq_candidates
        res = []
        def recur(i, nums, sumv):
            if sumv == target:
                res.append(nums[:])
            elif sumv > target:
                return
            elif i >= len(uniq_candidates):
                return
            else:
                cnt = 0
                cand = uniq_candidates[i]
                while sumv <= target and cnt <= counter.get(cand):
                    recur(i + 1, nums, sumv)
                    nums.append(cand)
                    sumv += cand
                    cnt += 1
                for _ in range(cnt):
                    nums.pop()
        recur(0, [], 0)
        return res
