class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        accu = [0] * (n + 1)
        for i, num in enumerate(nums):
            accu[i+1] = accu[i] + num

        l1_max = [(0, None)] * n
        l2_max = [(0, None)] * n
        l3_max = [(0, None)] * n
        
        for i in range(n-k, -1, -1):
            if i == n - 1 or accu[i+k] - accu[i] >= l1_max[i+1][0]:
                l1_max[i] = (accu[i+k] - accu[i], i)
            else:
                l1_max[i] = l1_max[i+1]
            
        for i in range(n-2*k, -1, -1):
            if accu[i+k] - accu[i] + l1_max[i+k][0] >= l2_max[i+1][0]:
                l2_max[i] = (accu[i+k] - accu[i] + l1_max[i+k][0], i)
            else:
                l2_max[i] = l2_max[i+1]
            
        for i in range(n-3*k, -1, -1):
            if accu[i+k] - accu[i] + l2_max[i+k][0] >= l3_max[i+1][0]:
                l3_max[i] = (accu[i+k] - accu[i] + l2_max[i+k][0], i)
            else:
                l3_max[i] = l3_max[i+1]
        
        i = l3_max[0][1]
        j = l2_max[i + k][1]
        z = l1_max[j + k][1]
        return [i, j, z]