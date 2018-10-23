
class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_map = collections.defaultdict(list)
        sum_map[0].append(0)
        sum_arr = [0]
        for i, num in enumerate(nums):
            accu_sum = sum_arr[-1] + num
            sum_arr.append(accu_sum)
            sum_map[accu_sum].append(i+1)
        
        n = len(nums)
        for i in range(1, n-3):
            seg_sum = sum_arr[i]
            accu_j = 2 * seg_sum + nums[i]
            for j in sum_map[accu_j]:
                if n - 2 > j > i + 1:
                    accu_k = 3 * seg_sum + nums[i] + nums[j]
                    for k in sum_map[accu_k]:
                        if n - 1 > k > j + 1 and sum_arr[-1] - sum_arr[k+1] == seg_sum:
                            return True
                        
        return False
    
# This failed [0,0,0.........0, 1]