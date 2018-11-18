class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        accu_sum = [0]
        for num in nums:
            accu_sum.append(accu_sum[-1] + num)
        
        j = 0
        max_avg = float(accu_sum[k]) / float(k)
        for i in range(k + 1, len(nums) + 1):
            # To find j such that nums[j:i] is largest average ending on i
            avg1 = float(accu_sum[i] - accu_sum[j]) / float(i - j)
            avg2 = float(accu_sum[i] - accu_sum[i-k]) / float(k)
            if avg2 >= avg1:
                j = i - k
            max_avg = max(max_avg, avg1, avg2)
        return max_avg

# This implementation is wrong
# j is optimal solution for i - 1
# Not necessarily j is also one of optimal for i
# we can rule out [0, j)
# but not (j, i - k]