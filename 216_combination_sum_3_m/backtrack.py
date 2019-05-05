class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        target = n

        def recur(i, nums, sumv):
            if len(nums) > k:
                return
            elif sumv == target and len(nums) == k:
                res.append(nums[:])
            elif sumv > target:
                return
            elif i < 1:
                return
            else:
                recur(i-1, nums, sumv)
                nums.append(i)
                recur(i-1, nums, sumv + i)
                nums.pop()
        recur(9, [], 0)
        return res