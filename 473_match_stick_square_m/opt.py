class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # [] is not covered, the below will return true instead
        if not nums:
            return False

        peri = sum(nums)
        if peri % 4 != 0:
            return False
        edge = peri / 4
        
        nums = sorted(nums, reverse=True)

        def recur(i, length):
            if i == len(nums):
                return True
            for j in range(4):
                if nums[i] + length[j] <= edge:
                    length[j] += nums[i]
                    if recur(i + 1, length):
                        return True
                    length[j] -= nums[i]
            return False
        
        if nums[0] > edge:
            return False

        length = [nums[0], 0, 0, 0]
        return recur(1, length)
        
# Why sorted reversed on line 16 will be MUCH faster.
# 
# Careful we need to check if nums[0] can be blindly assigned to edge 0 now
# 
# Key idea to summarize
# 1. DFS on nums index for sure, assign each number label of 0, 1, 2, 3
# 2. Utilize the symmetric by setting nums[0] to one of them
# 3. Sorted ascending, then we can prune early case when the gap is too small so no afterwards number can fit in the gap
# 4. Sorting descending is much faster. 