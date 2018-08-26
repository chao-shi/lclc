class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        return self.mtable(nums, m)

    def mtable(self, nums, m):
        n = len(nums)
        if m > n:
            return -1

        self.indexSum(nums)
        self.n = n
        self.mtable={}
        return self.recur3(0, m)

    def recur3(self, i, m):
        if m == 1:
            return self.sums[self.n] - self.sums[i]
        
        if (i, m) in self.mtable:
            return self.mtable[(i, m)]

        minv = self.sums[self.n] - self.sums[i]
        for j in range(i+1, self.n - m + 2):
            rightminmax = self.recur3(j, m-1)
            minv = min(minv, max(rightminmax, self.sums[j] - self.sums[i]))

            if rightminmax <= self.sums[j] - self.sums[i]:
                break

        self.mtable[(i, m)] = minv
        return minv
        
    def indexSum(self, nums):
        self.nums = nums
        self.sums = [0]
        sumv = 0
        for num in nums:
            sumv = sumv + num
            self.sums.append(sumv)