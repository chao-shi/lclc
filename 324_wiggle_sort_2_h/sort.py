class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        snums = sorted(nums, reverse = True)
        i, j  = n/2, 0
        ans = []
        while len(ans) < n:
            if i < n:
                ans.append(snums[i])
            if j < n/2:
                ans.append(snums[j])
            i, j = i + 1, j + 1
        
        for i in range(n):
            nums[i] = ans[i]

# O(NlogN) time and O(N) space