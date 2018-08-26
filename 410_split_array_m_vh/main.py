class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # Can I divide in a way such that each seg sum <= max_sum
        def test(max_sum):
            seg_start, seg_sum, seg_cnt = 0, 0, 0
            for j, num in enumerate(nums):
                seg_sum += num
                if seg_sum > max_sum:
                    # Don't worry that nums[j] > max_sum,
                    # we control input
                    seg_start = j
                    seg_sum = nums[j]
                    seg_cnt += 1
            # Don't forget here
            seg_cnt += 1
            return seg_cnt <= m
        
        # A value will always be found
        lb, hb = max(nums), sum(nums)
        while lb <= hb:
            mid = (lb + hb) / 2
            if test(mid):
                hb = mid - 1
            else:
                lb = mid + 1
        return lb