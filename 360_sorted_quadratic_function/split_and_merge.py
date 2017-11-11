# 49ms
class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        def func(x):
            return a*x**2 + b*x + c
        
        # Step 1: Split the array to nums[:i] and nums[i:] 
        # both sorted by final function value.
        if a != 0:
            i = bisect.bisect_left(nums, b/(-2.0 * a))      # Float number!!!
            if a > 0:
                nums[:i] = nums[i-1::-1]        # Easy mistake here nums[a:b:-1] means nums[b+1:a+1] in reverse order
            else:                               # Easier to think about as for loop
                nums[i:] = nums[:i-1:-1]
        elif b > 0:
            i = 0
        else:
            i = len(nums)
            nums = nums[::-1]
        
        # Step 2 merge it
        
        s, t = 0, i
        res = []
        while len(res) < len(nums):
            if s == i:
                res.append(func(nums[t]))
                t += 1
            elif t == len(nums):
                res.append(func(nums[s]))
                s += 1
            elif func(nums[s]) < func(nums[t]):
                res.append(func(nums[s]))
                s += 1
            else:
                res.append(func(nums[t]))
                t += 1
        return res