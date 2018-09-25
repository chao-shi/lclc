class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_num = max(nums)
        mask = 1
        cnt = 0
        while mask <= max_num:
            cnt1 = 0
            for num in nums:
                if num & mask > 0:
                    cnt1 += 1
            cnt += (len(nums) - cnt1) * cnt1
            mask <<= 1
        return cnt