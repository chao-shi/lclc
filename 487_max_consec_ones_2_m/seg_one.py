class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def find_next_one_seg(nums):
            i = 0
            while i < len(nums):
                if nums[i] == 0:
                    i += 1
                else:
                    j = i
                    while j < len(nums) and nums[j] == 1:
                        j += 1
                    yield (i, j)
                    i = j

        # Corner case empty
        if not nums:
            return 0

        # Corner case no 1 segments
        maxv = 1
        last_s, last_t = None, None
        for s, t in find_next_one_seg(nums):
            l = t - s
            if t < len(nums) or s > 0:
                l += 1
            maxv = max(maxv, l)

            if last_t == s - 1:
                maxv = max(maxv, t - last_s)
            last_s, last_t = s, t
        return maxv


