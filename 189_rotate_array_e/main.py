class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        n = len(nums)
        k %= n
        
        def reverse(s, i, j):
            j -= 1
            while i < j:
                s[i], s[j] = s[j], s[i]
                i, j = i + 1, j - 1
        
        reverse(nums, 0, len(nums))
        reverse(nums, 0, k)
        reverse(nums, k, len(nums))