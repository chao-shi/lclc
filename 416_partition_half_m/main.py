class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def findSum(nums, sum):
            sum_set = set()
            for num in nums:
                new_sums = [s + num for s in sum_set] + [num]
                for new_sum in new_sums:
                    sum_set.add(new_sum)
                
                if sum in sum_set:
                    return True
            return False
        
        total_sum = sum(nums)
        return findSum(nums, total_sum / 2) if total_sum % 2 == 0 else False