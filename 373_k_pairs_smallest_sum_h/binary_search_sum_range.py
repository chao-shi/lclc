class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []

        bar = self.findBar(nums1, nums2, k)
        cands, j = [], len(nums2) - 1
        for i in range(len(nums1)):
            while j >=0 and nums2[j] + nums1[i] > bar:
                j -= 1
            cands.extend([[nums1[i], nums2[jj]]for jj in range(j+1)])
            
        cands = sorted(cands, key=lambda x:x[0] + x[1])
        return cands[:min(k, len(cands))]

        
    def findBar(self, nums1, nums2, k):
        # look for first value in [li, hi] such that there are at least k pairs <= value
        li, hi = nums1[0] + nums2[0], nums1[-1] + nums2[-1]
        while li <= hi:
            mid = (li + hi) / 2
            smallerEqual = len(nums1) * len(nums2) - self.countBigger(nums1, nums2, mid)
            
            if smallerEqual == k:
                return mid
            elif smallerEqual > k:
                hi = mid - 1
            else:
                li = mid + 1
        return li
            
    def countBigger(self, nums1, nums2, value):
        cnt, j = 0, len(nums2) - 1
        for i in range(len(nums1)):
            while j >=0 and nums2[j] + nums1[i] > value:
                j -= 1
            cnt += len(nums2) - (j + 1)
        return cnt

# M is the range of integers
# n is the size of input of nums1 and nums2
# O(logM * n) for findBar (Actually it is O(n))
# O(k) for 14-17 and O(K * logK) for sorting 
# if we can find a good bar

# In good case: complexity is O(n) + O(K * logK)

# However, what if we have a bar not so good,
# A lot of duplicates around the bar

