class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        def check_bigger_than_all(avg):
            # check if there is a subarray of at least k with sum > 0
            # Return False if there is one
            sub_nums = [num - avg for num in nums]
            accu_sum = [0]
            for sub_num in sub_nums:
                accu_sum.append(accu_sum[-1] + sub_num)

            min_accu = 0
            for i in range(k, len(nums) + 1):
                max_sum = accu_sum[i] - min_accu
                if max_sum > 0:
                    return False
                min_accu = min(min_accu, accu_sum[i - k + 1])
            return True
        
        # lb, hb = -sys.maxint, sys.maxint
        # I though too much from gradient of accu sum
        lb, hb = min(nums), max(nums)
        while hb - lb > 10 ** (-5):
            mid = float(hb + lb) / 2.0
            if check_bigger_than_all(mid):
                hb = mid
            else:
                lb = mid
        return lb
    
# 1. All average sum must be range of [min(nums), max(nums)]
# 2. Use binary search to solve it.
# 3. To test if a proposed average is bigger than all average.

# Assume that nums[i:j+1] has higher average than x
#    (nums[i]+nums[i+1]+...+nums[j])/(j-i+1)>x
#     =>nums[i]+nums[i+1]+...+nums[j]>x*(j-i+1)
#     =>(nums[i]-x)+(nums[i+1]-x)+...+(nums[j]-x)>0