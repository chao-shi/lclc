class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # a+b-c-d = S
        # Which means a+b=c+d+S
        # We just need to find all subset of a, b, c, d, S sum to half of total sum
        # Then divide by 2
        sum_all = sum(nums) + abs(S)
        if sum_all % 2 != 0 or sum_all - S < S:
            return 0
        
        target = sum_all / 2
        
        cnt = [1] + [0] * target
        for num in nums:
            for i in range(len(cnt) - 1, num - 1, -1):
                cnt[i] += cnt[i - num]
        
        # cnt[0] = 1 because there is empty set, but empty is not a valid solution
        # Needs to exclude
        return cnt[-1] if len(nums) != 0 else 0
    
# Careful line 12 needs abs(S)
        
# Smart O(N, K) = O(N-1, K - i) + O(N-1, K)
# How to avoid creating temp storage by iterating backwards