
class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        sum_map = collections.defaultdict(list)
        sum_map[0].append(0)
        sum_arr = [0]
        for i, num in enumerate(nums):
            accu_sum = sum_arr[-1] + num
            sum_arr.append(accu_sum)
            sum_map[accu_sum].append(i+1)
        
        jk_map = collections.defaultdict(set)
        for j in range(2, n-2):
            for k in range(j + 2, n - 1):
                seg_sum_1 = sum_arr[k] - sum_arr[j + 1]
                seg_sum_2 = sum_arr[-1] - sum_arr[k + 1]
                if seg_sum_1 == seg_sum_2:
                    jk_map[j].add(seg_sum_1)
        
        for i in range(1, n-3):
            seg_sum = sum_arr[i]
            accu_j = 2 * seg_sum + nums[i]
            for j in sum_map[accu_j]:
                if n - 2 > j > i + 1:
                    if seg_sum in jk_map[j]:
                        return True
        return False

# Find k by precalculating
# For each j, what can be the segment sum of sum(j+1:k) and sum(k+1:)