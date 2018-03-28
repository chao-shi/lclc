class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq = collections.deque()
        i = 0
        res = [] 
        for j in range(len(nums)):
            # update left
            if j - i >= k:
                if dq[0] == nums[i]:
                    dq.popleft()
                i += 1
                
            # update right
            while dq and dq[-1] < nums[j]:
                dq.pop()
            dq.append(nums[j])
            
            # get max
            if j - i + 1 == k:
                res.append(dq[0])
        return res
            
            