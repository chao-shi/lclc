class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}
        for i, ch in enumerate(t):
            if ch not in dict:
                dict[ch] = []
            dict[ch].append(i)

        j = -1
        for ch in s:
            indexes = dict.get(ch, [])
            j = self.firstBigger(j, indexes)
            if j == None:
                return False
        return True
    
    def firstBigger(self, target, nums):
        li, hi = 0, len(nums) - 1
        while li <= hi:
            mid = (li + hi) / 2
            if nums[mid] > target:
                hi = mid - 1
            else:                    
                li = mid + 1
        return nums[li] if li < len(nums) else None
    
    