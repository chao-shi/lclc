class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Could implement a O(N) for median as well.
        def median(nums):
            nums = sorted(nums)
            if len(nums) % 2 == 0:
                return (nums[len(nums)/2-1] + nums[len(nums)/2]) / 2.0
            else:
                return nums[len(nums) / 2]

        m, n = len(grid), len(grid[0])
        xs = [i for i in range(m) for j in range(n) if grid[i][j]]
        ys = [j for i in range(m) for j in range(n) if grid[i][j]]
        mx, my = median(xs), median(ys)
        return int(sum(abs(x - mx) for x in xs) + sum(abs(y - my) for y in ys))