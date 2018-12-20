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

        minv = [min(nums[i+1:]) for i in range(n-1)]

        def recur(i):
            if i == n:
                return True
            num = nums[i]
            for ii in range(k):
                if (ii == 0 or set_sum[ii-1] > 0) and set_sum[ii] + num <= target:
                    assigned[i] = ii
                    set_sum[ii] += num
                    if recur(i + 1):
                        return True
                    set_sum[ii] -= num
            return False
        
        return recur(0)


# line 25, don't skip the empty set, make the set assigning continous