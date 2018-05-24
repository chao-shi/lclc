class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Link list loop detection
        # Each state is some numbe in the given array
        # next(n) is nums[n], which is always valid
        # If we write out the chain of numbers, for sure there will be some repeating element
        # beause the state is finite
        # For example, n = 4 and nums [3, 4, 1, 4, 2]
        # The number chaining is 3, 4, 2, 1, 4....
        
        # Since 4 is the first recuring number and the 3, 1 are its index
        # the index is different, so 4 is the duplicated numbers (both nums[1] and nums[3] are 4)
        
        def next(n):
            return nums[n]

        sp = next(nums[0])
        fp = next(sp)
        
        
        # Loop guranteed
        while sp != fp:
            sp = next(sp)
            fp = next(next(fp))
            
        sp = nums[0]
        while sp != fp:
            sp, fp = next(sp), next(fp)
        return sp