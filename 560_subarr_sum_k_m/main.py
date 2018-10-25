class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        accu_sum_map = collections.defaultdict(int)
        accu_sum_map[0] = 1
        accu_sum = 0
        res = 0
        for num in nums:
            accu_sum += num
            res += accu_sum_map[accu_sum - k]
            accu_sum_map[accu_sum] += 1
        return res
        