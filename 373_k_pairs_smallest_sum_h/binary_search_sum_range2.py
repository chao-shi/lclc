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

        # last value bar such that there are "cnt" pairs smaller or equal to bar and cnt <= k 
        bar, cnt = self.findBar(nums1, nums2, k)
        shortage = k - cnt # Need this many from bar + 1

        cands = []
        for i in range(len(nums1)):
            j = 0
            while j < len(nums2) and (nums1[i] + nums2[j] <= bar or (nums1[i] + nums2[j] == bar + 1 and shortage > 0)):
                cands.append([nums1[i], nums2[j]])
                if nums1[i] + nums2[j] == bar + 1:
                    shortage -= 1
                j += 1

        cands = sorted(cands, key=lambda x:x[0] + x[1])
        return cands[:min(k, len(cands))]

        
    def findBar(self, nums1, nums2, k):
        # look for last value in [li, hi] such that there are no more than k pairs <= value
        li, hi = nums1[0] + nums2[0], nums1[-1] + nums2[-1]
        while li <= hi:
            mid = (li + hi) / 2
            smallerEqual = len(nums1) * len(nums2) - self.countBigger(nums1, nums2, mid)
            
            if smallerEqual > k:
                hi = mid - 1
            else:
                li = mid + 1
        return hi, len(nums1) * len(nums2) - self.countBigger(nums1, nums2, hi)
            
    def countBigger(self, nums1, nums2, value):
        cnt, j = 0, len(nums2) - 1
        for i in range(len(nums1)):
            while j >=0 and nums2[j] + nums1[i] > value:
                j -= 1
            cnt += len(nums2) - (j + 1)
        return cnt

# This runs in 116ms OJ
# But in theory it is better than binary_search_sum_range.py because it better handles duplicated values

# Slight change of how we define the bar
# inside findBar
# remove early termination on mid
# return hi instead

# After we get bar, we know how many we need from bar + 1, the value is stored inside counter "shortage"

# In main function, we get rid of the two pointer approach. Reset j to start every time.