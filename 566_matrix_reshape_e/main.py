class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums
        k = 0
        new_nums = [[0] * c for i in range(r)]
        for i in range(r):
            for j in range(c):
                new_nums[i][j] = nums[k/n][k%n]
                k += 1
        return new_nums
                