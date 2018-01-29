class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # wrong
        # i, j, k = len(nums1) - 1, len(nums2) - 1, len(nums1) + len(nums2) - 1

        i, j, k = m - 1, n - 1, m + n - 1
        # k - i is the unused elements in nums2, which is always be positive
        while k >= 0:
            if j == -1 or (i >= 0 and nums1[i] > nums2[j]):
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

# Careful about useage of n, m , don't mix with len()