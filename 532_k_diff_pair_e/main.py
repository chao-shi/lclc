class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        elif k == 0:
            cnt = collections.Counter(nums)
            return len([num for num in cnt if cnt[num] > 1])
        else:
            cnt = 0
            nums = set(nums)
            for num in nums:
                if num + k in nums:
                    cnt += 1
            return cnt

# Careful for case <=0