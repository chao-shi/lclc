class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        cnt = collections.Counter(nums)
        n = len(nums)
        res = []

        def recur(cnt, prefix, n):
            if len(prefix) == n:
                res.append(list(prefix))

            for v in set(cnt.keys()):
                cnt[v] -= 1
                if cnt[v] == 0:
                    del cnt[v]
                prefix.append(v)
                recur(cnt, prefix, n)
                prefix.pop()
                cnt[v] += 1

        recur(cnt, [], len(nums))
        return res
