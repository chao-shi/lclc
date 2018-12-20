class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_sum = sum(nums)
        
        if num_sum % k != 0:
            return False

        n = len(nums)
        assigned = [None] * n
        set_sum = [0] * k
        target = num_sum / k

        def recur(i):
            if i == n:
                return True
            num = nums[i]
            for ii in range(k):
                if set_sum[ii] + num <= target:
                    assigned[i] = ii
                    set_sum[ii] += num
                    if recur(i + 1):
                        return True
                    set_sum[ii] -= num
            return False
        
        return recur(0)

# This approach assign a group for each number at a time.