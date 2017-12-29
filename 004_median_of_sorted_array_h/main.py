class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if (len(nums1) + len(nums2)) % 2 == 1:
            maxv = -sys.maxint
            if nums1: maxv = max(nums1[-1], maxv)
            if nums2: maxv = max(nums2[-1], maxv)
            maxv += 1
            nums1.append(maxv)
            leftmin, righmax = self.findMidTwo(nums1, nums2)
            return leftmin
        else:
            leftmin, rightmax = self.findMidTwo(nums1, nums2)
            return (leftmin + rightmax) / 2.0
            
        
    def findMidTwo(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n, m = len(nums1), len(nums2)
        
        lb, hb = 0, n
        
        while lb <= hb:
            i = (lb + hb) / 2
            j = (n + m) / 2 - i
            # if (j == 0 or i == n or nums1[i] >= nums2[j-1]) and (j == m or i == 0 or nums2[j] >= nums1[i-1]):
            # simplify to
            if (i == n or nums1[i] >= nums2[j - 1]) and (i == 0 or nums2[j] >= nums1[i - 1]):
                leftmax, rightmin = -sys.maxint, sys.maxint
                if i > 0: leftmax = max(leftmax, nums1[i-1])
                if j > 0: leftmax = max(leftmax, nums2[j-1])
                if i < n: rightmin = min(rightmin, nums1[i])
                if j < m: rightmin = min(rightmin, nums2[j])
                return leftmax, rightmin
            elif i < n and nums1[i] < nums2[j-1]:
                # should include i as well in the left
                lb = i + 1
            else:
                hb = i - 1