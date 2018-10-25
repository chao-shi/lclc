class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        used = set()
        max_len = 0
        for i in range(len(nums)):
            p = i
            cnt = 0
            while p not in used:
                used.add(p)
                cnt += 1
                p = nums[p]
            max_len = max(max_len, cnt)
        return max_len
    
# Optimization, prove that loops does not cross. 
# Suppose that i -> j
# Then there is no other ii which points to j
# Prove: If there is, then A[ii] = A[i], which contradicts to the uniqueness.
            