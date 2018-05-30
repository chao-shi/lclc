class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # assuming two bolloons at both end that never burst
        nums = [1] + nums + [1]
        # 2D matrix handles mt[i][i] = 0 nicely
        mt = [[0] * len(nums) for i in range(len(nums))]
        
        for length in range(1, len(nums) - 1):
            for i in range(1, len(nums) - length):
                j = i + length
                maxv = 0
                # k is last burst
                for k in range(i, j):
                    maxv = max(maxv, nums[k] * nums[i-1] * nums[j] + mt[i][k] + mt[k+1][j])
                mt[i][j] = maxv
        return mt[1][len(nums) - 1]
        