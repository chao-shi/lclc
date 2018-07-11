class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        m1 = {}
        for num in nums1:
            m1[num] = 1
        m2 = {}
        res = []
        for num in nums2:
            if num in m1 and not num in m2:
                res.append(num)
            m2[num] = 1
        return res