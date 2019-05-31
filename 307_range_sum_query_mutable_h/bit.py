import math
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        if self.n > 0:
            bitlen = int(math.ceil(math.log(self.n, 2)))
            maxlen = 2 ** bitlen
        else:
            maxlen = 0

        self.bit = [0] * (maxlen + 1)
        accu_sum = [0] * (maxlen + 1)

        for i in range(1, len(accu_sum)):
            accu_sum[i] = accu_sum[i-1] + (nums[i-1] if i - 1 < len(nums) else 0)

        for i in range(1, len(self.bit)):
            self.bit[i] = accu_sum[i] - accu_sum[i&(i-1)]

        self.nums = nums


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        delta = val - self.nums[i]
        self.nums[i] = val
        i += 1

        while i < len(self.bit):
            self.bit[i] += delta
            #i = i & (i-1)
            i += i & (-i) 
            # i & (-i) return the larget 2 power which divides i

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sumBeginRange(j+1) - self.sumBeginRange(i) 


    def sumBeginRange(self, i):
        sumv = 0
        while i > 0:
            sumv += self.bit[i]
            i = i & (i-1)
        return sumv

sol =  NumArray([9, -8])
sol.update(0, 3)
print sol.sumRange(1, 1)
print sol.sumRange(0, 1)
sol.update(1, -3)
print sol.sumRange(0, 1)